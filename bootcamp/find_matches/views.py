from django.shortcuts import render, get_object_or_404
from adviseher.models import Profile

def index(request):
    match_list = Profile.objects.order_by('id')[:5] #
    context = {'match_list': match_list}
    return render(request, 'find_matches/index.html', context)
def profile(request, profile_id): #view of single profile
    profile = get_object_or_404(Profile, pk=profile_id)
    return render(request, 'find_matches/profile.html', {'profile': profile})
