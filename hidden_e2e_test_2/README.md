## Test Case: `test_multiple_snapshots`

## Overview

This document describes a unit test that verifies the functionality of creating, saving, and restoring multiple inventory snapshots. It ensures that multiple snapshots can be independently created and loaded, verifying that the inventory management system maintains consistency throughout the process.

### Purpose

The purpose of this test is to verify the following:
1. The system can save and manage multiple snapshots of the inventory.
2. Each snapshot correctly captures the state of the inventory at the time of its creation.
3. Loading any saved snapshot restores the inventory state as expected.
4. Deleting snapshots prevents them from being used to restore the inventory.

### Test Details

- **Test Name**: `test_multiple_snapshots`
- **Sequence of Operations**:
  1. **Define and Add Items**:
     - Define an item of type "widget" and add 20 units.
  2. **Save First Snapshot**:
     - Save the initial state of the inventory, resulting in `snapshot_id_1`.
  3. **Modify Inventory**:
     - Add more "widget" items(30) and define a new item type "gadget"(10) with additional units.
  4. **Save Second Snapshot**:
     - Save the modified inventory state, resulting in `snapshot_id_2`.
  5. **Further Modify Inventory**:
     - Remove some units from the "widget" item.
  6. **Load First Snapshot**:
     - Load the inventory from `snapshot_id_1` and verify that only the initial "widget" inventory is restored with count 20.
  7. **Load Second Snapshot**:
     - Load the inventory from `snapshot_id_2` and verify both "widget" and "gadget" inventories are restored with count 50 & 10.
  8. **Delete Snapshots**:
     - Delete both snapshots and confirm that they cannot be used to restore inventory after deletion.
    
### Note

