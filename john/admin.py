from django.contrib import admin
from .models import Home, About, Profile, Category, Skills, Portfolio, Books, News


# Home
admin.site.register(Home)


# About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
     inlines = [
        ProfileInline,
    ]






# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]


# Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    model = Portfolio
    extra = 3



admin.site.register(Books)
admin.site.register(News)
