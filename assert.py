import sender_stand_request

def test_Check_that_the_response_code_is_200():
    assert sender_stand_request.get_orders_track().status_code == 200

# Подрезов Андрей, 6-я когрорта финальный проект