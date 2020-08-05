from django.shortcuts import render, redirect
from .models import Blogs

# Create your views here.


def blog_admin_index(request):
    context = {
        'blogs': Blogs.objects.all().reverse(),
    }
    return render(request, 'owner/blog_index.html', context)


def view_blog(request, blog_id):
    context = {
        'blog': Blogs.objects.get(id=blog_id)
    }
    return render(request, 'owner/view_blog.html', context)


def create_blog(request):
    if request.POST:
        blog = Blogs.objects.create(
            title=request.POST['title'], description=request.POST['description'], content=request.POST['content'])
        return render(request, 'owner/blog_img_select.html',  {'id': blog.id})
    return render(request, 'owner/blog_create.html')


def img_selection(request, img_link=None, id=None):
    if img_link != None and id != None:
        blog = Blogs.objects.get(id=id)
        blog.img_link = img_link
        blog.save()
        return redirect('/salon_blog')
    return render(request, 'owner/blog_img_select.html')
# def modify_blog(request, post_id):
# 	if request.POST :
# 		blog = Blog.objects.get(id=post_id)
# 		blog.title = request.POST['rh_title']
# 		blog.description = request.POST['rh_description']
# 		blog.content = request.POST['rh_content']
# 		blog.save()
# 		return redirect(f'/view/{post_id}')
# 	context = {
# 	'blog' : Blog.objects.get(id=post_id) ,
# 	'title' : 'Update your blog',
# 	'btn_text': 'Update'
# 	}
# 	return render(request, 'create_post.html', context)

# def create_blog(request):
# 	if request.POST:
# 		Blog.objects.create(title=request.POST['rh_title'],
# 							description=request.POST['rh_description'],
# 						 	content=request.POST['rh_content'],
# 						 	img_link= 'https://images.unsplash.com/photo-1580618672591-eb180b1a973f?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjIyNjM5fQ' )
# 		# adding a temp img_link so if the user quits the porcess of selection of teh image in between the content written in safe
# 		request.session['blog_id'] = Blog.objects.latest('id').id
# 		print('this is the latest created blog id bitch ', request.session['blog_id'])
# 		context = {}
# 		return render(request,'img_select.html', context)
# 	context = {
# 		'title' : 'Create a new post',
# 		 'btn_text': 'Update'
# 	}

# 	return render(request,'create_post.html', context)

# def show_images(request,img_link):
# 	blog = Blog.objects.get(id=request.session['blog_id'])
# 	blog.img_link = img_link
# 	blog.save()
# 	return redirect('/')

# def delete_post(request, post_id, confirmation=0):
# 	if confirmation == 1 :
# 		Blog.objects.get(id=post_id).delete()
# 		return redirect('/')
# 	return render(request, 'confirmation.html')

# def create_user(request):
# 	if request.POST:
# 		User.objects.create(user_name=request.POST['username'], password=request.POST['password'])
# 		return redirect('/')
# 	return render(request,'create_user.html')
