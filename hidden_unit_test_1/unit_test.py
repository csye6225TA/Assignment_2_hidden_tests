@patch('requests.post')
def test_delete_data_failure(self, mock_post):
    # Simulate server response for an invalid snapshot ID
    mock_post.return_value.json.return_value = {'result': -1}
    
    # Create an instance of the InventoryClient
    client = InventoryClient("http://localhost:5000")
    
    # Attempt to delete a snapshot with an invalid ID
    response = client.delete_data('invalid-id')
    
    # Verify that the response matches the expected failure output
    self.assertEqual(response, {'result': -1})
    
    # Ensure that the mocked request was called with the correct parameters
    mock_post.assert_called_once_with(
        'http://localhost:5000/delete_data',
        headers={'Content-Type': 'application/json'},
        data=json.dumps({"snapshot_id": "invalid-id"})
    )
