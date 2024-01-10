from healdata_utils import utils


def test_add_missing_fields():
    # data (note one var not in schema)
    data = [
        {"var2": 2, "var3": 3, "var1": 1},
        {
            "var5": 10,
            "var4": 9,
            "var1": 1,
        },
    ]
    # fields from schema
    fields = ["var1", "var2", "var3", "var4"]

    data_with_missing = utils.sync_fields(data, fields)
    assert data_with_missing == [
        {"var1": 1, "var2": 2, "var3": 3, "var4": None},
        {"var1": 1, "var2": None, "var3": None, "var4": 9, "var5": 10},
    ]


def test_unflatten_jsonpath():
    input = {
        "module": "Testing",
        "constraints.enum": "1|2|3|4",
        "standardsMappings[1].item.url": "http//:helloitem1",
        "standardsMappings[0].item.url": "http//:helloitem2",
        "standardsMappings[1].instrument.url": "http//:helloworld4",
        "test1.test2.test3[1]": "test3_1",
        "test1.test2.test3[0].test4": "test4_1",
    }

    output = {
        "module": "Testing",
        "constraints": {"enum": "1|2|3|4"},
        "standardsMappings": [
            {"item": {"url": "http//:helloitem2"}},
            {
                "item": {"url": "http//:helloitem1"},
                "instrument": {"url": "http//:helloworld4"},
            },
        ],
        "test1": {"test2": {"test3": [{"test4": "test4_1"}, {"test3": "test3_1"}]}},
    }
    field_json = utils.unflatten_jsonpath(input)
    assert field_json == output,"Problem with converting input dictionary to output dictionary"
