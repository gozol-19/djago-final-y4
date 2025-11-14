from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Item, OrderItem, Order, Payment, Coupon, Refund, Address, UserProfile

# Custom UserProfile Admin
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'
    fk_name = 'user'
    extra = 0

# Extend User Admin
class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super().get_inline_instances(request, obj)

# Order Admin
def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)
make_refund_accepted.short_description = 'Update orders to refund granted'

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered', 'being_delivered', 'received',
                    'refund_requested', 'refund_granted', 'shipping_address',
                    'billing_address', 'payment', 'coupon']
    list_display_links = ['user', 'shipping_address', 'billing_address',
                         'payment', 'coupon']
    list_filter = ['ordered', 'being_delivered', 'received',
                  'refund_requested', 'refund_granted']
    search_fields = ['user__username', 'ref_code']
    actions = [make_refund_accepted]

# Address Admin
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'street_address', 'apartment_address',
                   'country', 'zip', 'address_type', 'default']
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']

# Item Admin (Simple)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount_price', 'category', 'label']
    list_filter = ['category', 'label']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}

# Payment Admin (Simple)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'timestamp']
    list_filter = ['timestamp']
    search_fields = ['user__username']

# Coupon Admin (Simple)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'amount']
    search_fields = ['code']

# Refund Admin (Simple)
class RefundAdmin(admin.ModelAdmin):
    list_display = ['order', 'reason', 'accepted']
    list_filter = ['accepted']
    search_fields = ['order__ref_code', 'reason']

# OrderItem Admin (Simple)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'item', 'quantity', 'ordered']
    list_filter = ['ordered']
    search_fields = ['user__username', 'item__title']

# Unregister default User admin and register custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register your other models
admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Refund, RefundAdmin)
admin.site.register(Address, AddressAdmin)