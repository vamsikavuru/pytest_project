import pytest
import pytest_check as check



def test_hard_assertion():
    print("check 1 started...")
    assert 1 == 1 "Test pass"
    print("check 1 completed...")

    print("check 2 started...")
    assert 2 == 2 "Test pass"
    print("check 2 completed...")

    print("check 3 started...")
    assert 3 == 3 "Test pass"
    print("check 3 completed...")


def test_soft_assertion():
    print("check 1 started...")
    check.is_true(1==1, "test pass")
    print("check 1 complete..")

    print("check 2 started...")
    check.is_true(2==2, "test pass")
    print("check 2 complete..")

    print("check 3 started...")
    check.is_true(3==3, "test pass")
    print("check 3 complete..")


@pytest.fixture(autouse=True)
def fixture_demo():
    print("Before Test Step")
    yield
    print("After Test Step")





