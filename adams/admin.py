from django.contrib import admin
from .models import (
    SiteMeta,
    HeroSection,
    About,
    Skill,
    Service,
    Project,
    Testimonial,
    ContactMessage,
    BlogPost,
    SocialLink,
)


@admin.register(SiteMeta)
class SiteMetaAdmin(admin.ModelAdmin):
    list_display = ("site_title", "tagline")
    
    search_fields = ("site_title",)


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "cta_text", "cta_link")
    search_fields = ("heading",)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "proficiency", "category")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "icon_class")
    search_fields = ("title",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "featured")
    search_fields = ("title", "tech_stack")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("featured",)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "position")
    search_fields = ("name", "position")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "sent_at")
    search_fields = ("name", "email", "subject")
    readonly_fields = ("sent_at",)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("created_at",)


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("platform", "url", "icon_class")
    search_fields = ("platform",)
