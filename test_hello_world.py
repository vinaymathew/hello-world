import runpy


def test_hello_world_script_runs(capsys):
    runpy.run_path("hello-world.py")
    captured = capsys.readouterr()

    assert "a first github trial" in captured.out
    assert "Testing github...seems to be a very powerful environment" in captured.out
