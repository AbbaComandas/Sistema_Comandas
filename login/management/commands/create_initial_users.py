from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = "Crea usuarios iniciales de prueba: admin, garzon, cocina, gerencia"

    def handle(self, *args, **options):
        usuarios = [
            {"username": "garzon", "password": "garzon", "nombre_completo": "Garzón Demo", "rol": "garzon", "is_superuser": False, "is_staff": False},
            {"username": "cocina", "password": "cocina", "nombre_completo": "Cocina Demo", "rol": "cocina", "is_superuser": False, "is_staff": False},
            {"username": "gerencia", "password": "gerencia", "nombre_completo": "Gerencia Demo", "rol": "gerencia", "is_superuser": False, "is_staff": False},
        ]

        for u in usuarios:
            user, created = User.objects.get_or_create(username=u["username"])
            user.nombre_completo = u["nombre_completo"]
            user.rol = u["rol"]
            user.is_active = True
            user.is_superuser = u["is_superuser"]
            user.is_staff = u["is_staff"]
            user.set_password(u["password"])
            user.save()
            estado = "creado" if created else "actualizado"
            self.stdout.write(self.style.SUCCESS(f'Usuario {estado}: {u["username"]} / {u["password"]} (rol: {u["rol"]})'))