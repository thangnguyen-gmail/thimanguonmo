from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from home.models import Product , Category, blog
# Create your views here.

def index(request):
    # trang chủ phải vào trong db lấy hết post ra để chuyển về trang index.html như phía dưới
    Products = Product.objects.all()
    context = {'posts': Products}
    return render(request, 'console/index.html',context ) 
    #return HttpResponse("Trang chu")
#truy cập trang chi tiết
def detail(request):
    context = {'post': Product.objects.get(pro_id=request.GET['id'])}
    return render(request, 'console/aboutus.html', context)
def aboutus(request):
    # Còn khi xem chi tiết bài viết thì phải vào db lấy cái bài viết cần xem ra rồi gửi về trang bên duwois để nó hiển thị ra
 

    return render(request,'console/aboutus.html')

