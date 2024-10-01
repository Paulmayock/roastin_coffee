from django.shortcuts import render, get_object_or_404, reverse, redirect

@login_required
def add_post(request):
    """
    View to add a blog post.
    """
    print(request.user)
    post_form = PostForm(request.POST, request.FILES)

    if request.method == 'POST':
        if post_form.is_valid():
            post_form = post_form.save(commit=False)
            post_form.title = post_form.title
            post_form.author = request.user
            post_form.status = 1
            post_form.save()
            return redirect(reverse('blog'))

    context = {
        'post_form': post_form
    }

    return render(request, 'blog/add_post.html', context)
