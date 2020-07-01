import pkg_resources
from pathlib import Path
from django.test import TestCase

_REQUIREMENTS_PATH = Path(__file__).parent.parent.with_name("requirements.txt")

class TestRequirements(TestCase):
  """Test availability of required packages."""

  def test_requirements(self):
    """Test that each required package is available."""
    requirements = pkg_resources.parse_requirements(_REQUIREMENTS_PATH.open())
    for requirement in requirements:
      requirement = str(requirement)
      with self.subTest(requirement=requirement):
        pkg_resources.require(requirement)
