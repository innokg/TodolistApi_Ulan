from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase): # создаем класс для проведения юнит-теста наследуем от APITestCase

    def test_creates_user(self): # каждый раз при импорте APITestCase мы получаем доступ ко всем assertion
        user = User.objects.create_user('innokg', 'ulan.developer@gmail.com', 'password123!@') # тестим функцию create_user
        self.assertIsInstance(user, User) # проверяем является ли user объектом класса User
        self.assertFalse(user.is_staff) # возвращает boolean
        self.assertEqual(user.email, 'ulan.developer@gmail.com')


    def test_creates_super_user(self):
        user = User.objects.create_superuser('innokg', 'ulan.developer@gmail.com', 'password123!@')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'ulan.developer@gmail.com')

    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username="",
                          email='ulan.developer@gmail.com', password='password123!@')

    def test_raises_error_with_message_when_no_username_is_supplied(self): # функция на выдачу ошибки если не указано имя пользователя
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_superuser(username='', email='ulan.developer@gmail.com', password='password123!@')


    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username="username",
                          email='', password='password123!@')

    def test_cant_create_super_user_with_no_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(
                username='username', email='ulan.developer@gmail.com', password='password123!@', is_staff=False)

    def test_cant_create_super_user_with_no_super_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(
                username='username', email='ulan.developer@gmail.com', password='password123!@', is_superuser=False)

    def test_creates_super_user(self):
        user = User.objects.create_superuser(
            'innokg', 'ulan.developer@gmail.com', 'password123!@')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'ulan.developer@gmail.com')