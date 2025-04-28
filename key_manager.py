import random
import string
from auth import Auth

def generate_key(length: int = 16) -> str:
    """生成随机卡密"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    auth = Auth()
    
    while True:
        print("\n卡密管理系统")
        print("1. 生成新卡密")
        print("2. 删除卡密")
        print("3. 查看所有卡密")
        print("4. 退出")
        
        choice = input("请选择操作 (1-4): ").strip()
        
        if choice == "1":
            days = int(input("请输入卡密有效期（天数）: "))
            key = generate_key()
            auth.add_key(key, days)
            print(f"已生成卡密: {key}")
            
        elif choice == "2":
            key = input("请输入要删除的卡密: ")
            auth.remove_key(key)
            print("卡密已删除")
            
        elif choice == "3":
            if not auth.keys:
                print("暂无卡密")
            else:
                for key, data in auth.keys.items():
                    expired = "已过期" if data.get("expired", False) else "有效"
                    print(f"卡密: {key} - 状态: {expired}")
                    
        elif choice == "4":
            break
            
        else:
            print("无效的选择，请重试")

if __name__ == "__main__":
    main() 