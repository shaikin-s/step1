import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")

@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")

@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def setup_browser(self):
        self.browser = webdriver.Chrome()

    def teardown_browser(self):
        self.browser.quit()


    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        # some checks
        self.browser.get(link)


    def test_second_smiling_faces(self, prepare_faces):
        # some checks
        self.browser.get(link)

