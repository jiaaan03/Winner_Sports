from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_aplikasi' : 'Winner Sports',
        'nama': 'Jihan Andita Kresnaputri',
        'kelas': 'PBP C'
    }

    return render(request, "main.html", context)
