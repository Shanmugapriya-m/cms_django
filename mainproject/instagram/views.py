from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, View
from .models import UserInfoModel, ContentModel
from .forms import ContentForm

# class UserRegistrationView(CreateView): 
#     template_name='instagram/registration.html'
#     model=UserInfoModel
#     fields='__all__'
#     success_url='/user'
#     def post(self, request, *args, **kwargs):
#         Email=request.POST['email']
#         if UserInfoModel.objects.filter(email=Email):
#             return self.get(request, *args, **kwargs)
#         return super().post(request, *args, **kwargs)
class UserRegistrationView(TemplateView):
    template_name='instagram/registration.html'
    def post(self, request, *args, **kwargs):
        UserInfoModel.objects.create(name=self.request.POST.get('name',None), 
                                     email=self.request.POST.get('email',None), 
                                     dateofbirth=self.request.POST.get('dateofbirth',None), 
                                     password=self.request.POST.get('password',None))
        # print(self.request.POST.get('name',None))
        # print(self.request.POST.get('email',None))
        # print(self.request.POST.get('dateofbirth',None))
        # print(self.request.POST.get('password',None))
        return redirect(reverse('login'))
        

    
    
    

class LoginView(TemplateView):
    template_name='instagram/login.html'
    def post(self, request, *args, **kwargs):
        Email=request.POST['email']
        password=request.POST['password']
        user = UserInfoModel.objects.filter(email=Email).first()
        if user:
            request.session['uid']=user.id
            return redirect(reverse('profile'))
        return self.get(request, *args, **kwargs)
    

class ProfileView(TemplateView):
    template_name='instagram/profile.html'
    def get(self, request, *args, **kwargs):
        u_id=request.session.get('uid')  
        try:
            user=UserInfoModel.objects.filter(id=u_id).first()
            if not user:
                return redirect(reverse('login'))
        except:
            return redirect(reverse('error'))
        kwargs['user']=user
        return super().get(request, *args, **kwargs) 


class LogoutView(View):
    def get(self, request, *agrs, **kwargs):
        u_id=request.session.get('uid')
        user=UserInfoModel.objects.filter (id=u_id).first()
        if user:
            del request.session['uid']
        return redirect(reverse('login'))


    # def get_context_data(self,**kwargs):
    #     print('name')
    #     user=kwargs['user']
    #     print(user.id) 
    #     print(user.dateofbirth)
    #     print(user.password)
    #     context={'user':user}
    #     kwargs.update(context)
    #     return kwargs

class CreatePageView(TemplateView):
    template_name='instagram/page.html'
    def get(self, request, *agrs, **kwargs):
        # ContentModel.objects.create(Title=self.request.POST.get('Title',None),
        #                             Image=self.request.POST.get('Image',None), 
        #                             Content=self.request.POST.get('Content',None),)
        return super().get(request, *agrs, **kwargs)

class CreateContentView(TemplateView):
    template_name='instagram/create_content.html'
    def post(self, request, *args, **kwargs):
        ContentModel.objects.create(title=self.request.POST.get('Title',None),
                                    image=self.request.POST.get('Image',None),
                                    content=self.request.POST.get('Content',None),
                                    created=self.request.POST.get('Create',None),
                                    updated=self.request.POST.get('Update',None),)
        return redirect(reverse('createpage'))
     
    def get_context_data(self, **kwargs):
        context = {
            'form': ContentForm
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)

class UpdateContentView(TemplateView):
    template_name='instagram/update_content.html'
    form_class=ContentForm
        
    def get_context_data(self, **kwargs):
        data=ContentModel.objects.get(id=self.kwargs['id'])
        form=self.form_class(instance=data)
        context={
            'form':form
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)
    def post(self, request, *args, **kwargs):
        data=ContentModel.objects.get(id=self.kwargs['id'])
        form=self.form_class(request.POST, instance=data)
        if form.is_valid():
            form.save() 
            return redirect(reverse('createpage'))
    #     d_id=kwargs.get('id')
    #     data=ContentModel.objects.get(id=d_id)
    #     context={'data':data}
    #     kwargs.update(context)
    #     return kwargs 
    # def POST(self, request, *agrs, **kwrgs):
    #     s_id= kwrgs.get('id')
    #     ContentModel.objects.filter(id=s_id).update()


class DeleteContentView(TemplateView):
    template_name='instagram/delete_content.html'
    def get(self, request, *args, **kwargs):
        
        return super().get(request, *args, **kwargs)   
        

class UserView(TemplateView):
    template_name='instagram/user.html'
    def get_context_data(self, **kwargs):
        some=UserInfoModel.objects.all()
        context={'page':some}
        kwargs.update(context)
        return super().get_context_data(**kwargs)

 