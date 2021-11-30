# python manage.py shell

from blogging.models import Post
from django.contrib.auth.models import User

all_users = User.objects.all()


p1 = Post(title="My First Post", text="this is the first post I''e written!", author=all_users[0])
p1.save()

# Checked the automatic date

p1.created_date
p1.modified_date

p2 = Post(title="Another post",
            text="The second one created",
            author=all_users[0]).save()

p3 = Post(title="The third one",
            text="With the word 'heffalump'",
            author=all_users[0]).save()

p4 = Post(title="Posters are a great decoration",
            text="When you are a poor college student",
            author=all_users[0]).save()

Post.objects.count()