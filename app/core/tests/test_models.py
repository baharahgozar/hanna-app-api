from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'baharahgozar@gmail.com'
        password = 'bahar181067'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'baharahgozar@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'bahar181067')
        self.assertEqual(user.email, email.lower())

def test_new_user_invalid_email(self):
    """test creating with no email raises error"""
    with self.assertRaises(ValueError):
        get_user_model().object.create_user(None, 'bahar181067')

def test_create_new_superuser(self):
    """Test creating a new superuser"""
    user = get_user_model().objects.create.superuser(
        'baharahgozar@gmail.com'
         'bahar181067'
    )



    self.assertTrue(user.is_superuser)
    self.assertTrue(user.is_staff)






















