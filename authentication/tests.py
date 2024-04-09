from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import UserProfile, IdentityDocument, VerificationVideo, IdentityVerification

CustomUser = get_user_model()

class TestModels(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@example.com', password='password123')
        self.user_profile = UserProfile.objects.create(user=self.user, full_name='John Doe', phone_number='123456789', email='john@example.com')
        self.identity_document = IdentityDocument.objects.create(user=self.user, document_type='Passport', document_number='123456789', document_image='identity_documents/passport.jpg')
        self.verification_video = VerificationVideo.objects.create(user=self.user, video='verification_videos/video.mp4')
        self.identity_verification = IdentityVerification.objects.create(user=self.user, verified=False)

    def test_user_profile_creation(self):
        self.assertEqual(self.user_profile.full_name, 'John Doe')
        self.assertEqual(self.user_profile.phone_number, '123456789')
        self.assertEqual(self.user_profile.email, 'john@example.com')

    def test_identity_document_creation(self):
        self.assertEqual(self.identity_document.document_type, 'Passport')
        self.assertEqual(self.identity_document.document_number, '123456789')
        self.assertEqual(self.identity_document.document_image.name, 'identity_documents/passport.jpg')

    def test_verification_video_creation(self):
        self.assertEqual(self.verification_video.video.name, 'verification_videos/video.mp4')

    def test_identity_verification_creation(self):
        self.assertFalse(self.identity_verification.verified)
