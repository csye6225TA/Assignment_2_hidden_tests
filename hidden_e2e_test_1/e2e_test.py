  def test_cr_save_load_delete_inventory(self):
      # Define a new item
      response = self.client.define_stuff("test", "A useful test")
      self.assertEqual(response, {'message': 'Defined type \'test\' with description \'A useful test\'.'})

      # Add items
      response = self.client.add(10, "test")
      self.assertEqual(response, {'message': 'Added 10 of type \'test\'.'})

      # Save the inventory
      save_response = self.client.save_data()
      self.assertIn('snapshot_id', save_response)
      snapshot_id = save_response['snapshot_id']

      # Remove all items and undefine them
      response = self.client.remove(10, "test")
      self.assertEqual(response, {'message': 'Removed 10 of type \'test\'.'})
      response = self.client.undefine("test")
      self.assertEqual(response, {'message': 'Undefined type \'test\'.'})

      # Load the inventory from the snapshot
      load_response = self.client.load_data(snapshot_id)
      self.assertEqual(load_response, {'result': 0})

      # Check if the item is back in the inventory with the correct count
      response = self.client.get_count("test")
      self.assertEqual(response, {'count': 10})

      # Delete the snapshot
      delete_response = self.client.delete_data(snapshot_id)
      self.assertEqual(delete_response, {'result': 0})

      # Verify the snapshot was deleted
      # Try to load from the deleted snapshot
      load_response_after_delete = self.client.load_data(snapshot_id)
      self.assertEqual(load_response_after_delete, {'result': -1})

      self.client.undefine("test")
