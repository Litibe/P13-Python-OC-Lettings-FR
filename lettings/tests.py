from django.test import Client
from django.urls import reverse, resolve
import pytest
from pytest_django.asserts import assertTemplateUsed

from lettings.models import Letting
from lettings.models import Address

client = Client()


def create_new_address():
    new_address = Address.objects.create(
        number=588,
        street="Argyle Avenue",
        city="East Meadow",
        state="NY",
        zip_code=11554,
        country_iso_code="USA"
    )
    return new_address


def create_new_letting(new_address):
    new_letting = Letting.objects.create(
        title="Underground Hygge",
        address=new_address
    )
    return new_letting


@pytest.mark.django_db
def test_01_lettings_index_without_data():
    # test_path
    path = reverse('lettings:index')
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings:index"
    # test_template
    response = client.get(path)
    assertTemplateUsed(response, 'lettings/index.html')
    # test_title_h1
    elementhtml = "<title>Lettings</title>"
    assert elementhtml.encode() in response.content
    elementhtml = "<h1>Lettings</h1>"
    assert elementhtml.encode() in response.content
    # test_links
    path_home = reverse('oc_lettings_site_index')
    elementhtml = '<a href="' + path_home + '">Home</a>'
    assert elementhtml.encode() in response.content
    path_profiles = reverse('profiles:index')
    elementhtml = '<a href="' + path_profiles + '">Profiles</a>'
    assert elementhtml.encode() in response.content
    # test_content
    elementhtml = 'No lettings are available.'
    assert elementhtml.encode() in response.content


@pytest.mark.django_db
def test_02_lettings_index_with_data():
    # test_path
    path = reverse('lettings:index')
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings:index"
    # test_template
    response = client.get(path)
    assertTemplateUsed(response, 'lettings/index.html')
    # test_title_h1
    elementhtml = "<title>Lettings</title>"
    assert elementhtml.encode() in response.content
    elementhtml = "<h1>Lettings</h1>"
    assert elementhtml.encode() in response.content
    # test_links
    path_home = reverse('oc_lettings_site_index')
    elementhtml = '<a href="' + path_home + '">Home</a>'
    assert elementhtml.encode() in response.content
    path_profiles = reverse('profiles:index')
    elementhtml = '<a href="' + path_profiles + '">Profiles</a>'
    assert elementhtml.encode() in response.content
    # test_content
    lettings = Letting.objects.all()
    for letting in lettings:
        elementhtml = letting.title
        assert elementhtml.encode() in response.content


@pytest.mark.django_db
def test_03_lettings_letting():
    address = create_new_address()
    letting = create_new_letting(address)
    # test_path
    path = reverse('lettings:letting', kwargs={"letting_id": letting.id})
    assert resolve(path).view_name == "lettings:letting"
    # test_template
    response = client.get(path)
    assertTemplateUsed(response, 'lettings/letting.html')
    # test_title_h1
    elementhtml = "<title>" + letting.title + "</title>"
    assert elementhtml.encode() in response.content
    elementhtml = "<h1>" + letting.title + "</h1>"
    assert elementhtml.encode() in response.content
    # test_content
    elementhtml = str(letting.address.number)
    assert elementhtml.encode() in response.content
    elementhtml = letting.address.street
    assert elementhtml.encode() in response.content
    elementhtml = letting.address.city
    assert elementhtml.encode() in response.content
    elementhtml = letting.address.state
    assert elementhtml.encode() in response.content
    elementhtml = str(letting.address.zip_code)
    assert elementhtml.encode() in response.content
    elementhtml = letting.address.country_iso_code
    assert elementhtml.encode() in response.content
    # test_links
    path_back = reverse('lettings:index')
    elementhtml = '<a href="' + path_back + '">Back</a>'
    assert elementhtml.encode() in response.content
    path_home = reverse('oc_lettings_site_index')
    elementhtml = '<a href="' + path_home + '">Home</a>'
    assert elementhtml.encode() in response.content
    path_profiles = reverse('profiles:index')
    elementhtml = '<a href="' + path_profiles + '">Profiles</a>'
    assert elementhtml.encode() in response.content
