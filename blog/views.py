from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import context
from django.template import defaulttags
from blog.models import Post, PostCategory, Comment
from blog import model_helpers
from blog import navigation


def post_list(request, category_name=model_helpers.post_category_all.slug()):
    # global category, posts
    category, posts = model_helpers.get_category_and_posts(category_name)
    categories = model_helpers

    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_POSTS),
        'category': category,
        'posts': posts,
        'categories': categories,
	}

    return render(request, 'blog/post_list.html', context)


# render(request, template_name, context=None, content_type=None, status=None, using=None)

# return render({'all_articles' : all_articles, 'message' : 'Write something!'},
#     'blog/index.html', context)



# def post_list(request, ):
#       posts = Post.objects.all()
#
#       context = {
#         'posts': posts,
# 	}
#       return render(request, 'blog/post_list.html', context)


def post_detail(request, post_id):

	post = get_object_or_404(Post, pk=post_id)
	posts_save_category = Post.objects.filter(published=True, category=post.category).exclude(pk=post_id)

	context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_POSTS),
        'post': post,
        'posts_save_category': posts_save_category,
   }
	return render(request, 'blog/post_detail.html', context)
