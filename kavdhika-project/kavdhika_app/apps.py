from django.apps import AppConfig


class KavdhikaAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kavdhika_app'
    
    def ready(self):
        """Register template tags when the app is ready."""
        from django.template.defaulttags import register
        try:
            import kavdhika_app.templatetags.custom_filters
        except ImportError:
            pass
