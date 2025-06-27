from django.db import models

# For file uploads like profile pictures, project screenshots
def upload_to(instance, filename):
    return f"{instance.__class__.__name__.lower()}/{filename}"

# -----------------------
# Core Site Configuration
# -----------------------
class SiteMeta(models.Model):
    site_title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=255, blank=True)
    logo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    favicon = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.site_title


class HeroSection(models.Model):
    heading = models.CharField(max_length=255)
    subheading = models.TextField()
    background_image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    cta_text = models.CharField("Call-to-action Text", max_length=50, blank=True)
    cta_link = models.URLField(blank=True)

    def __str__(self):
        return "Hero Section"


# -----------------------
# About Section
# -----------------------
class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    profile_image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return self.title


# -----------------------
# Skills and Services
# -----------------------
class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField(help_text="Enter value from 0 to 100")
    category = models.CharField(max_length=50, blank=True)  # e.g., Frontend, Backend

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=100, help_text="Font Awesome class, e.g., 'fa fa-code'")

    def __str__(self):
        return self.title


# -----------------------
# Projects
# -----------------------
class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255, help_text="Comma-separated technologies")
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# -----------------------
# Testimonials
# -----------------------
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    photo = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return f"Testimonial from {self.name}"


# -----------------------
# Contact Messages
# -----------------------
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"


# -----------------------
# Blog (Optional)
# -----------------------
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# -----------------------
# Social Links
# -----------------------
class SocialLink(models.Model):
    platform = models.CharField(max_length=50)  # e.g., Twitter, LinkedIn
    url = models.URLField()
    icon_class = models.CharField(max_length=100, help_text="e.g., 'fab fa-twitter'")

    def __str__(self):
        return self.platform
