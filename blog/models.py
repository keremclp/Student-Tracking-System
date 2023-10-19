from django.db import models

# Models
from account.models import User
# Third Party App:
from autoslug import AutoSlugField
from tinymce import models as tinymce_models


class CommonModel(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ('title',)

class Tag(CommonModel):

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse(
    #         "blog:tag_view",
    #         kwargs={"tag_slug": self.slug}
    #     )

class Category(CommonModel):

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse(
    #         "blog:category_view",
    #         kwargs={"category_slug": self.slug},
    #     )

class BlogPost(CommonModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    cover_image = models.ImageField(upload_to='post')
    content = tinymce_models.HTMLField(blank=True, null=True)
    view_count = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created_at',)

    # def get_absolute_url(self):
    #     return reverse(
    #         "read:post_detail_view",
    #         kwargs={
    #             "user_slug": self.user.profile.slug,
    #             "post_slug": self.slug
    #         },
    #     )
    # def get_post_edit_url(self):
    #     return reverse(
    #         "blog:post_edit_view",
    #         kwargs={
    #             "post_slug": self.slug
    #         },
    #     )