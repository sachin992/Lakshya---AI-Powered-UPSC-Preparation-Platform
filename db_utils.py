import sqlite3
from datetime import datetime
from typing import List, Dict, Optional

DB_PATH = "BPSC_Lakshya_users.db"

class DatabaseManager:
    """Centralized database management for Dalvoy application"""
    
    @staticmethod
    def get_connection():
        """Get database connection"""
        return sqlite3.connect(DB_PATH)
    
    @staticmethod
    def get_user_profile(user_id: int) -> Optional[Dict]:
        """Fetch complete user profile"""
        conn = DatabaseManager.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, full_name, email, phone, bpsc_attempt, 
                   commitment_4hrs, created_at, last_login
            FROM users WHERE id = ?
        """, (user_id,))
        
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return {
                "id": user[0],
                "full_name": user[1],
                "email": user[2],
                "phone": user[3],
                "bpsc_attempt": user[4],
                "commitment_4hrs": user[5],
                "created_at": user[6],
                "last_login": user[7]
            }
        return None
    
    @staticmethod
    def update_user_profile(user_id: int, full_name: str = None, 
                           phone: str = None, bpsc_attempt: str = None) -> bool:
        """Update user profile information"""
        try:
            conn = DatabaseManager.get_connection()
            cursor = conn.cursor()
            
            if full_name:
                cursor.execute("UPDATE users SET full_name = ? WHERE id = ?", (full_name, user_id))
            if phone:
                cursor.execute("UPDATE users SET phone = ? WHERE id = ?", (phone, user_id))
            if bpsc_attempt:
                cursor.execute("UPDATE users SET bpsc_attempt = ? WHERE id = ?", (bpsc_attempt, user_id))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error updating profile: {e}")
            return False
    
    @staticmethod
    def get_all_users() -> List[Dict]:
        """Fetch all users (admin function)"""
        conn = DatabaseManager.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, full_name, email, phone, bpsc_attempt, created_at, last_login
            FROM users ORDER BY created_at DESC
        """)
        
        users = cursor.fetchall()
        conn.close()
        
        return [
            {
                "id": u[0],
                "full_name": u[1],
                "email": u[2],
                "phone": u[3],
                "bpsc_attempt": u[4],
                "created_at": u[5],
                "last_login": u[6]
            }
            for u in users
        ]
    
    @staticmethod
    def get_user_stats() -> Dict:
        """Get user statistics"""
        conn = DatabaseManager.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM users")
        total_users = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM users WHERE commitment_4hrs = 1")
        committed_users = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM users WHERE last_login IS NOT NULL")
        active_users = cursor.fetchone()[0]
        
        conn.close()
        
        return {
            "total_users": total_users,
            "committed_users": committed_users,
            "active_users": active_users
        }
    
    @staticmethod
    def delete_user(user_id: int) -> bool:
        """Delete a user (admin function)"""
        try:
            conn = DatabaseManager.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False
    
    @staticmethod
    def change_password(user_id: int, new_password_hash: str) -> bool:
        """Change user password"""
        try:
            conn = DatabaseManager.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE users SET password_hash = ? WHERE id = ?
            """, (new_password_hash, user_id))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error changing password: {e}")
            return False
    
    @staticmethod
    def export_user_data(user_id: int) -> Optional[Dict]:
        """Export complete user data"""
        conn = DatabaseManager.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT * FROM users WHERE id = ?
        """, (user_id,))
        
        columns = [description[0] for description in cursor.description]
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return dict(zip(columns, user))
        return None