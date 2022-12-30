from django.test import TestCase

# Create your tests here.
# def index(request):
#     # return HttpResponse("Hello world!")
#     template=loader.get_template('index.html')
#     return HttpResponse(template.render())
# def base(request):
#     template=loader.get_template('base.html')
#     return HttpResponse(template.render())

# class GetALLFactory(APIView):

#     def get(self, request):
#         try: 
#             id = request.query_params["idFactory"]
#             if id != None:
#                 list_factory=factory.objects.get(idFactory=id)
#                 mydata=GetAllFactory(list_factory,many=False)
#         except:
#             list_factory= factory.objects.all()
#             mydata=GetAllFactory(list_factory,many=True)
#         return Response(data=mydata.data,status=status.HTTP_200_OK)
        
#     def post(self,request):
#         dataadd=GetAllFactory(data=request.data)
#         if dataadd.is_valid():
#             dataadd.save()
#             return Response(data=dataadd.data,status=status.HTTP_200_OK)
#         return Response(dataadd.errors,status=status.HTTP_200_OK)

#     def put(self, request):
#         id = request.query_params["idFactory"]
#         editFactory=factory.objects.get(idFactory=id)
#         dataadd=GetAllFactory(instance=editFactory,data=request.data)
#         if dataadd.is_valid():
#             dataadd.save()
#             return Response(data=dataadd.data,status=status.HTTP_200_OK)
#         return Response(dataadd.errors,status=status.HTTP_200_OK)
#     def delete(self,request):
#         id = request.query_params["idFactory"]
#         deleteFactory=factory.objects.get(idFactory=id)
#         deleteFactory.delete()
#         return Response("Delete Success")

# class GetALLProduct(APIView):

#     def get(self, request):
#         try: 
#             id = request.query_params["idProduct"]
#             if id != None:
#                 list_Product=product.objects.get(idProduct=id)
#                 mydata=GetAllProduct(list_Product,many=False)
#         except:
#             list_Product= product.objects.all()
#             mydata=GetAllProduct(list_Product,many=True)
#         return Response(data=mydata.data,status=status.HTTP_200_OK)
        
#     def post(self,request):
#         dataadd=GetAllProduct(data=request.data)
#         if dataadd.is_valid():
#             dataadd.save()
#             return Response(data=dataadd.data,status=status.HTTP_200_OK)
#         return Response(dataadd.errors,status=status.HTTP_200_OK)

#     def put(self, request):
#         id = request.query_params["idProduct"]
#         editProduct=product.objects.get(idProduct=id)
#         dataadd=GetAllProduct(instance=editProduct,data=request.data)
#         if dataadd.is_valid():
#             dataadd.save()
#             return Response(data=dataadd.data,status=status.HTTP_200_OK)
#         return Response(dataadd.errors,status=status.HTTP_200_OK)
#     def delete(self,request):
#         id = request.query_params["idProduct"]
#         deleteProduct=product.objects.get(idProduct=id)
#         deleteProduct.delete()
#         return Response("Delete Success")
        
# class GetALLProduce(APIView):

#     def get(self, request):
#         try: 
#             id = request.query_params["idProduct"]
#             if id != None:
#                 list_Product=product.objects.get(idProduct=id)
#                 mydata=GetAllProduct(list_Product,many=False)
#         except:
#             list_Product= product.objects.all()
#             mydata=GetAllProduct(list_Product,many=True)
#         return Response(data=mydata.data,status=status.HTTP_200_OK)
        
#     def post(self,request):
#         dataadd=GetAllProduct(data=request.data)
#         if dataadd.is_valid():
#             dataadd.save()
#             return Response(data=dataadd.data,status=status.HTTP_200_OK)
#         return Response(dataadd.errors,status=status.HTTP_200_OK)

#     def put(self, request):
#         id = request.query_params["idProduct"]
#         editProduct=product.objects.get(idProduct=id)
#         dataadd=GetAllProduct(instance=editProduct,data=request.data)
#         if dataadd.is_valid():
#             dataadd.save()
#             return Response(data=dataadd.data,status=status.HTTP_200_OK)
#         return Response(dataadd.errors,status=status.HTTP_200_OK)
#     def delete(self,request):
#         id = request.query_params["idProduct"]
#         deleteProduct=product.objects.get(idProduct=id)
#         deleteProduct.delete()
#         return Response("Delete Success")