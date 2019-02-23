from django.contrib import admin

from .models import Course, CourseReview, CourseLink


class CourseLinkAdmin(admin.ModelAdmin):
    list_display = ['url_title', 'url', 'course']
    fields = ('url_title', 'url_description', 'img_url', 'url', 'course')

    class Meta:
        model = CourseLink


class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'author', 'timestamp']
    fields = ('text', 'author')

    class Meta:
        model = CourseReview


class CourseAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    fields = ('name', 'course_code', 'class_year', 'reviews')
    filter_horizontal = ['reviews']

    class Meta:
        model = Course


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseReview, CourseReviewAdmin)
admin.site.register(CourseLink, CourseLinkAdmin)