from django.test import Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
import pytest
from pytest_django.asserts import assertTemplateUsed

from profiles.models import Profile


client = Client()


def create_new_user():
    new_user = User.objects.create_user(
        first_name="Bob",
        last_name="TOTO",
        username="Boby",
        email="bob@example.com",
        password="abc123")
    return new_user


def create_new_profile(new_user):
    new_profile = Profile.objects.create(
        user=new_user,
        favorite_city="Paris"
    )
    return new_profile


@pytest.mark.django_db
def test_01_profiles_index_without_data():
    # test_path
    path = reverse('profiles:index')
    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles:index"
    # test_template
    response = client.get(path)
    assertTemplateUsed(response, 'profiles/index.html')
    # test_title_h1
    elementhtml = "<title>Profiles</title>"
    assert elementhtml.encode() in response.content
    elementhtml = "<h1>Profiles</h1>"
    assert elementhtml.encode() in response.content
    # test_links
    path_home = reverse('oc_lettings_site_index')
    elementhtml = '<a href="' + path_home + '">Home</a>'
    assert elementhtml.encode() in response.content
    path_profiles = reverse('lettings:index')
    elementhtml = '<a href="' + path_profiles + '">Lettings</a>'
    assert elementhtml.encode() in response.content
    # test_contenu
    elementhtml = "No profiles are available."
    assert elementhtml.encode() in response.content


@pytest.mark.django_db
def test_02_profiles_index_with_data():
    new_user = create_new_user()
    new_profile = create_new_profile(new_user)
    # test_path
    path = reverse('profiles:index')
    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles:index"
    # test_template
    response = client.get(path)
    assertTemplateUsed(response, 'profiles/index.html')
    # test_title_h1
    elementhtml = "<title>Profiles</title>"
    assert elementhtml.encode() in response.content
    elementhtml = "<h1>Profiles</h1>"
    assert elementhtml.encode() in response.content
    # test_links
    path_home = reverse('oc_lettings_site_index')
    elementhtml = '<a href="' + path_home + '">Home</a>'
    assert elementhtml.encode() in response.content
    path_profiles = reverse('lettings:index')
    elementhtml = '<a href="' + path_profiles + '">Lettings</a>'
    assert elementhtml.encode() in response.content
    # test_contenu
    response = client.get(path)
    elementhtml = new_user.username
    assert elementhtml.encode() in response.content
    path_profiles = reverse('profiles:profile',
                            kwargs={"username": new_profile.user.username})
    elementhtml = '<a href="' + path_profiles + '">'
    assert elementhtml.encode() in response.content


@pytest.mark.django_db
def test_03_profiles_profile():
    new_user = create_new_user()
    new_profile = create_new_profile(new_user)
    # test_path
    path = reverse('profiles:profile',
                   kwargs={"username": new_profile.user.username})
    assert path == "/profiles/" + new_profile.user.username + "/"
    assert resolve(path).view_name == "profiles:profile"
    # test_template
    response = client.get(path)
    assertTemplateUsed(response, 'profiles/profile.html')
    # test_title_h1
    elementhtml = "<title>" + new_profile.user.username + "</title>"
    assert elementhtml.encode() in response.content
    elementhtml = "<h1>" + new_profile.user.username + "</h1>"
    assert elementhtml.encode() in response.content
    # test_links
    path_back = reverse('profiles:index')
    elementhtml = '<a href="' + path_back + '">Back</a>'
    assert elementhtml.encode() in response.content
    path_home = reverse('oc_lettings_site_index')
    elementhtml = '<a href="' + path_home + '">Home</a>'
    assert elementhtml.encode() in response.content
    path_profiles = reverse('lettings:index')
    elementhtml = '<a href="' + path_profiles + '">Lettings</a>'
    assert elementhtml.encode() in response.content
    # test_contenu
    elementhtml = str(new_profile.user.first_name)
    assert elementhtml.encode() in response.content
    elementhtml = str(new_profile.user.last_name)
    assert elementhtml.encode() in response.content
    elementhtml = str(new_profile.user.email)
    assert elementhtml.encode() in response.content
    elementhtml = str(new_profile.favorite_city)
    assert elementhtml.encode() in response.content
