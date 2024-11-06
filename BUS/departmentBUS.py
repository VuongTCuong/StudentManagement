from DAL import departmentDAL
from DTO import departmentDTO
class departmentBUS:
    def __init__(self):
        self.departmentDAL = departmentDAL.departmentDAL()
    
    def add_department(self, makhoa, tenkhoa):
        return self.departmentDAL.add_department(makhoa, tenkhoa)
    
    def get_all_department(self):
        return self.departmentDAL.get_all_department()
    
    def update_department(self, makhoa, tenkhoa):
        try:
            # Create department object with updated data
            department = departmentDTO.departmentDTO(makhoa, tenkhoa)
            # Call DAO to update in database
            result = self.departmentDAL.update_department(department)
            return result
        except Exception as e:
            print(f"Error in DepartmentBUS - update_department: {str(e)}")
            return False
    
    def delete_department(self, makhoa):
        try:
            # First check if department is referenced in other tables
            if self.is_department_in_use(makhoa):
                return False
            
            # If not in use, proceed with deletion
            result = self.departmentDAL.delete_department(makhoa)
            return result
        except Exception as e:
            print(f"Error in DepartmentBUS - delete_department: {str(e)}")
            return False
    
    def get_department_by_id(self, makhoa):
        return self.departmentDAL.get_department_by_id(makhoa)
    
    def is_department_in_use(self, makhoa):
        return self.departmentDAL.check_department_in_students(makhoa) > 0
    
    
    
    