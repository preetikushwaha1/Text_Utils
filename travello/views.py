from django.shortcuts import render
from travello.models import blog

# Create your views here.

def index(request):
    """blog1 = blog()
    blog1.post_By = 'Preeti'
    blog1.discription = "i have chnaged the desciption of first blog"
    blog1.img ="blog-image.jpg"
    blog1.like = 700
    blog1.offer = False

    blog2 = blog()
    blog2.post_By ="kiran"
    blog2.discription ="i have changed the description of second blog"
    blog2.img ="blog-image0.jpg"
    blog2.like ="900"
    blog2.offer = True

    blog3 = blog()
    blog3.post_By ="Ashu"
    blog3.discription ="i have changed the description of third blog"
    blog3.img ="London.jpg"
    blog3.like ="1000"
    blog3.offer = False
    blog_list =[blog1,blog2, blog3]
    """

    blog_list = blog.objects.all()

    return render(request, 'index.html', {'blog_list' : blog_list })   