# 🌸 Sistema de Comandas — Hotel Abba

**Una plataforma web centralizada para gestionar pedidos, cocina y gerencia del Hotel Abba**, 
construida con 💚 **Django 5.2** y amor por la organización perfecta.

---

## 🪄 Requisitos previos

Antes de comenzar, asegúrate de tener instalado:

- 🐍 **Python 3.13+**
- 🌿 **pip** (gestor de paquetes)
- ⚙️ **Git**
- 💻 **Visual Studio Code** o el editor que más te guste
- 🌐 **Navegador web moderno** (para entrar a tu `localhost`)

---

## 🧁 Instalación paso a paso

### 1️⃣ Clonar el proyecto

```bash
git clone https://github.com/NegritaW/Sistema_Comandas.git
cd Sistema_Comandas
```

---

### 2️⃣ Crear y activar el entorno virtual

```bash
python -m venv SistemaComandas
SistemaComandas\Scripts\activate
```

(Si usas Linux/Mac: `source SistemaComandas/bin/activate`)

---

### 3️⃣ Instalar dependencias

```bash
pip install django
```

> Si tienes un archivo `requirements.txt`, también puedes usar:
> ```bash
> pip install -r requirements.txt
> ```

---

### 4️⃣ Realizar las migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

Esto creará las tablas necesarias (incluyendo `django_session`, `auth_user`, etc.).

---

### 5️⃣ Crear usuarios iniciales automáticos 🍓

El proyecto incluye un **comando personalizado** que genera usuarios base (garzón, cocina y gerencia).  
Para ejecutarlo:

```bash
python manage.py create_initial_users
```

📋 **Usuarios generados automáticamente:**

| Usuario  | Contraseña | Rol       | Activo |
|-----------|-------------|-----------|---------|
| garzon    | garzon      | Garzón    | ✅ |
| cocina    | cocina      | Cocina    | ✅ |
| gerencia  | gerencia    | Gerencia  | ✅ |

> 💡 El superusuario (admin) se crea manualmente con:
> ```bash
> python manage.py createsuperuser
> ```

---

### 6️⃣ Levantar el servidor ✨

```bash
python manage.py runserver
```

Luego entra a:

🌐 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

El sistema redirigirá automáticamente al login.

---

## 💄 Estructura principal del proyecto

```
Sistema_Comandas/
│
├── Sistema_Comandas/          # Configuración general del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── login/                     # App principal (login + roles)
│   ├── views.py               # Lógica de login, registro y redirecciones
│   ├── urls.py
│   ├── forms.py
│   ├── models.py
│   └── management/commands/   # Comando create_initial_users.py
│
├── templates/                 # Archivos HTML compartidos
│   ├── base.html
│   ├── login.html
│   ├── registro.html
│   └── home.html
│
└── static/
    ├── css/
    │   └── estilos.css        # Estilo verde elegante + logout rojo 🔥
    └── img/
        └── abba-hotels-logo.png
```

---

## 💚 Características principales

- 🔐 **Sistema de login y registro** con validación y mensajes de error elegantes.  
- 👑 **Roles personalizados:** garzón, cocina, gerencia, administrador.  
- 💤 **Usuarios nuevos inactivos hasta aprobación del admin.**  
- 🎨 **Diseño base consistente:** encabezado verde, logo del Hotel Abba y botón rojo de logout.  
- 💅 **Formularios centrados y estilizados**, perfectos para desktop o tablet.  
- 🧰 **Comando de creación inicial (`create_initial_users`)** para ambientes de desarrollo.

---

## 💕 Créditos

Creado con cariño por **Ivy Pradines y su equipo de desarrollo** ✨  
Desarrolladora creativa del **INACAP Puerto Montt**.  
Inspirado en los estándares de Django, la hospitalidad del Hotel Abba y un toque girly💖
