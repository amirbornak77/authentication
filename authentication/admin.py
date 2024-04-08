from django.contrib import admin
from . models import  IdentityDocument, VerificationVideo, IdentityVerification
# Register your models here.

# Register in admin
@admin.register(IdentityDocument)
class IdentityDocumentAdmin(admin.ModelAdmin):
    list_display = ('user', 'document_type', 'document_number', 'document_image')

@admin.register(VerificationVideo)
class VerificationVideoAdmin(admin.ModelAdmin):
    list_display = ('user', 'video')

@admin.register(IdentityVerification)
class IdentityVerificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'verified')