@pytest.mark.parametrize("num_of_symbols", [2047, 2048, 2049])
def test_update_conference_session_description(self, num_of_symbols):
    with allure.step("description_chek_big_num_of_symbols"):
        conference_session_join = self.session

        symbol = "a"
        count = len(symbol)

        for i in range(count, num_of_symbols):
            symbol += "a"

        data = {
            "description": {
                "value": symbol
            }
        }
        if 2049 != num_of_symbols:
            res = self.api.update_conference_session_with_http_info(data, self.session, async_req=False)
            assert res[1] == 204, "cant update conf session with long description"
        else:
            try:
                self.api.update_conference_session_with_http_info(data, self.session, async_req=False)
                assert False, 'This method did\'t crash for symbol count is 2049'
            except:
                var = traceback.format_exc()
                assert check_error_stacktrace(var, 400), 'The error code is 400'

