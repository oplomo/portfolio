from django.shortcuts import render
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


from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


def home_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            subject = f"Message from {name}"
            full_message = f"From: {name} <{email}>\n\nMessage:\n{message}"
            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,
                ["adamsquare.dev@gmail.com"],
            )
            messages.success(request, "Your message has been sent successfully!")
        else:
            messages.error(request, "Please fill out all the fields.")

    context = {
        "site_meta": SiteMeta.objects.first(),
        "hero_section": HeroSection.objects.first(),
        "about": About.objects.first(),
        "skills": Skill.objects.all(),
        "services": Service.objects.all(),
        "projects": Project.objects.all(),
        "testimonials": Testimonial.objects.all(),
        "social_links": SocialLink.objects.all(),
        "blog_posts": BlogPost.objects.all().order_by("-created_at")[:5],
    }
    return render(request, "show/home.html", context)
