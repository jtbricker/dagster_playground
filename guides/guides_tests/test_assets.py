from guides.assets import (
    get_total_size,
    diamond
)

def test_get_total_size():
    file_sizes = { 'file1': 400, 'file2': 50 }
    result = get_total_size(file_sizes)
    assert result == 450


def test_diamond():
    res = diamond.execute_in_process()
    assert res.success
    assert res.output_for_node("get_total_size") > 0