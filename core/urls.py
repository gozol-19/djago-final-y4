# from django.urls import path
# from .views import (
#     ItemDetailView,
#     CheckoutView,
#     HomeView,
#     OrderSummaryView,
#     add_to_cart,
#     remove_from_cart,
#     remove_single_item_from_cart,
#     PaymentView,
#     AddCouponView,
#     RequestRefundView,
#     OrderConfirmationView,
#     # Admin Views
#     AdminDashboardView,
#     AdminProductListView, AdminProductCreateView, AdminProductUpdateView, AdminProductDeleteView,
#     AdminOrderListView, AdminOrderUpdateView,
#     AdminUserListView, AdminUserUpdateView,
#     AdminCouponListView, AdminCouponCreateView, AdminCouponUpdateView, AdminCouponDeleteView,
#     AdminPaymentListView,
#     AdminRefundListView, AdminRefundUpdateView,
#     ProfileView
# )
# from django.urls import include

# app_name = 'core'

# urlpatterns = [
#     # ===== CUSTOMER URLS =====
#     path('', HomeView.as_view(), name='home'),
#     path('checkout/', CheckoutView.as_view(), name='checkout'),
#     path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
#     path('product/<slug>/', ItemDetailView.as_view(), name='product'),
#     path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
#     path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
#     path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
#     path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
#          name='remove-single-item-from-cart'),
#     path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
#     path('order-confirmation/', OrderConfirmationView.as_view(), name='order-confirmation'),
#     path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
#     path('profile/', ProfileView.as_view(), name='profile'),
    
#     # ===== ADMIN URLS =====
#     path('admin-dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
    
#     # Product Management
#     path('admin/products/', AdminProductListView.as_view(), name='admin-product-list'),
#     path('admin/products/create/', AdminProductCreateView.as_view(), name='admin-product-create'),
#     path('admin/products/<int:pk>/update/', AdminProductUpdateView.as_view(), name='admin-product-update'),
#     path('admin/products/<int:pk>/delete/', AdminProductDeleteView.as_view(), name='admin-product-delete'),
    
#     # Order Management
#     path('admin/orders/', AdminOrderListView.as_view(), name='admin-order-list'),
#     path('admin/orders/<int:pk>/update/', AdminOrderUpdateView.as_view(), name='admin-order-update'),
    
#     # User Management
#     path('admin/users/', AdminUserListView.as_view(), name='admin-user-list'),
#     path('admin/users/<int:pk>/update/', AdminUserUpdateView.as_view(), name='admin-user-update'),
    
#     # Coupon Management
#     path('admin/coupons/', AdminCouponListView.as_view(), name='admin-coupon-list'),
#     path('admin/coupons/create/', AdminCouponCreateView.as_view(), name='admin-coupon-create'),
#     path('admin/coupons/<int:pk>/update/', AdminCouponUpdateView.as_view(), name='admin-coupon-update'),
#     path('admin/coupons/<int:pk>/delete/', AdminCouponDeleteView.as_view(), name='admin-coupon-delete'),
    
#     # Payment Management
#     path('admin/payments/', AdminPaymentListView.as_view(), name='admin-payment-list'),
    
#     # Refund Management
#     path('admin/refunds/', AdminRefundListView.as_view(), name='admin-refund-list'),
#     path('admin/refunds/<int:pk>/update/', AdminRefundUpdateView.as_view(), name='admin-refund-update'),
    
#     # Authentication
#     path('accounts/', include('allauth.urls')),
# ]


from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    OrderConfirmationView,
    # Admin Views
    AdminDashboardView,
    AdminProductListView, AdminProductCreateView, AdminProductUpdateView, AdminProductDeleteView,
    AdminOrderListView, AdminOrderUpdateView,
    AdminUserListView, AdminUserUpdateView,
    AdminCouponListView, AdminCouponCreateView, AdminCouponUpdateView, AdminCouponDeleteView,
    AdminPaymentListView,
    AdminRefundListView, AdminRefundUpdateView,
    ProfileView
)
from django.urls import include

app_name = 'core'

urlpatterns = [
    # ===== CUSTOMER URLS =====
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('order-confirmation/', OrderConfirmationView.as_view(), name='order-confirmation'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
    # ===== ADMIN URLS =====
    # Changed from 'admin-dashboard' to 'dashboard' for consistency
    path('dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
    
    # Product Management - changed prefix from 'admin/' to 'dashboard/'
    path('dashboard/products/', AdminProductListView.as_view(), name='admin-product-list'),
    path('dashboard/products/create/', AdminProductCreateView.as_view(), name='admin-product-create'),
    path('dashboard/products/<int:pk>/update/', AdminProductUpdateView.as_view(), name='admin-product-update'),
    path('dashboard/products/<int:pk>/delete/', AdminProductDeleteView.as_view(), name='admin-product-delete'),
    
    # Order Management
    path('dashboard/orders/', AdminOrderListView.as_view(), name='admin-order-list'),
    path('dashboard/orders/<int:pk>/update/', AdminOrderUpdateView.as_view(), name='admin-order-update'),
    
    # User Management
    path('dashboard/users/', AdminUserListView.as_view(), name='admin-user-list'),
    path('dashboard/users/<int:pk>/update/', AdminUserUpdateView.as_view(), name='admin-user-update'),
    
    # Coupon Management
    path('dashboard/coupons/', AdminCouponListView.as_view(), name='admin-coupon-list'),
    path('dashboard/coupons/create/', AdminCouponCreateView.as_view(), name='admin-coupon-create'),
    path('dashboard/coupons/<int:pk>/update/', AdminCouponUpdateView.as_view(), name='admin-coupon-update'),
    path('dashboard/coupons/<int:pk>/delete/', AdminCouponDeleteView.as_view(), name='admin-coupon-delete'),
    
    # Payment Management
    path('dashboard/payments/', AdminPaymentListView.as_view(), name='admin-payment-list'),
    
    # Refund Management
    path('dashboard/refunds/', AdminRefundListView.as_view(), name='admin-refund-list'),
    path('dashboard/refunds/<int:pk>/update/', AdminRefundUpdateView.as_view(), name='admin-refund-update'),
    
    # Authentication
    path('accounts/', include('allauth.urls')),
]