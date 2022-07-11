from django.test import Client
from django.urls import reverse, resolve
from pytest_django.asserts import assertTemplateUsed


client = Client()


def test_template_oc_lettings_site_index():
    # test_chemin
    path = reverse('oc_lettings_site_index')
    assert path == "/"
    assert resolve(path).view_name == "oc_lettings_site_index"
    # test_template
    response = client.get(path)
    assertTemplateUsed(response, 'oc_lettings_site/index.html')
    assert response.status_code == 200
    # test_title_h1
    elementhtml = "<title>Holiday Homes</title>"
    assert elementhtml.encode() in response.content
    elementhtml = "<h1>Welcome to Holiday Homes</h1>"
    assert elementhtml.encode() in response.content
    # test_contenu
    path_profiles = reverse('profiles:index')
    elementhtml = '<a href="' + path_profiles + '">Profiles</a>'
    assert elementhtml.encode() in response.content
    path_lettings = reverse('lettings:index')
    elementhtml = '<a href="' + path_lettings + '">Lettings</a>'
    assert elementhtml.encode() in response.content
