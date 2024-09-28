def test_multiple_snapshots(self):
    # Define items and add initial inventory
    response = self.client.define_stuff("widget", "A useful widget")
    self.assertEqual(response, {'message': 'Defined type \'widget\' with description \'A useful widget\'.'})
    
    response = self.client.add(20, "widget")
    self.assertEqual(response, {'message': 'Added 20 of type \'widget\'.'})

    # Save first snapshot
    save_response_1 = self.client.save_data()
    self.assertIn('snapshot_id', save_response_1)
    snapshot_id_1 = save_response_1['snapshot_id']

    # Modify inventory after first snapshot
    response = self.client.add(30, "widget")
    self.assertEqual(response, {'message': 'Added 30 of type \'widget\'.'})

    response = self.client.define_stuff("gadget", "A useful gadget")
    self.assertEqual(response, {'message': 'Defined type \'gadget\' with description \'A useful gadget\'.'})

    response = self.client.add(10, "gadget")
    self.assertEqual(response, {'message': 'Added 10 of type \'gadget\'.'})

    # Save second snapshot
    save_response_2 = self.client.save_data()
    self.assertIn('snapshot_id', save_response_2)
    snapshot_id_2 = save_response_2['snapshot_id']

    # Further modify inventory after second snapshot
    response = self.client.remove(10, "widget")
    self.assertEqual(response, {'message': 'Removed 10 of type \'widget\'.'})

    # Load the first snapshot and verify inventory
    load_response_1 = self.client.load_data(snapshot_id_1)
    self.assertEqual(load_response_1, {'result': 0})

    response = self.client.get_count("widget")
    self.assertEqual(response, {'count': 20})

    response = self.client.get_count("gadget")
    self.assertEqual(response, {'count': -1})

    # Load the second snapshot and verify inventory
    load_response_2 = self.client.load_data(snapshot_id_2)
    self.assertEqual(load_response_2, {'result': 0})

    response = self.client.get_count("widget")
    self.assertEqual(response, {'count': 50}) 

    response = self.client.get_count("gadget")
    self.assertEqual(response, {'count': 10}) 

    # Delete both snapshots
    delete_response_1 = self.client.delete_data(snapshot_id_1)
    self.assertEqual(delete_response_1, {'result': 0})

    delete_response_2 = self.client.delete_data(snapshot_id_2)
    self.assertEqual(delete_response_2, {'result': 0})

    # Verify snapshots were deleted
    load_deleted_1 = self.client.load_data(snapshot_id_1)
    self.assertEqual(load_deleted_1, {'result': -1})

    load_deleted_2 = self.client.load_data(snapshot_id_2)
    self.assertEqual(load_deleted_2, {'result': -1})

    # Clean up by undefining items
    self.client.undefine("widget")
    self.client.undefine("gadget")
