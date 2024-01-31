import streamlit as st
import pandas as pd
import sqlalchemy

# 数据库连接函数
def get_connection():
    return sqlalchemy.create_engine("mysql+pymysql://root:xzy031103@localhost:3306/zoomanagementsystem")

# 添加动物信息到数据库
def add_animal(engine, name, species, age, gender, health_status, area_id):
    with engine.connect() as connection:
        query = sqlalchemy.text(
            "INSERT INTO animal_info (Name, Species, Age, Gender, Health_Status, Area_ID) VALUES (:name, :species, :age, :gender, :health_status, :area_id)"
        )
        connection.execute(query, {"name": name, "species": species, "age": age, "gender": gender, "health_status": health_status, "area_id": area_id})

# 更新动物信息
def update_animal(engine, animal_id, name, species, age, gender, health_status, area_id):
    with engine.connect() as connection:
        query = sqlalchemy.text(
            "UPDATE animal_info SET Name = :name, Species = :species, Age = :age, Gender = :gender, Health_Status = :health_status, Area_ID = :area_id WHERE Animal_ID = :animal_id"
        )
        connection.execute(query, {"animal_id": animal_id, "name": name, "species": species, "age": age, "gender": gender, "health_status": health_status, "area_id": area_id})

# 删除动物信息
def delete_animal(engine, animal_id):
    with engine.connect() as connection:
        query = sqlalchemy.text(
            "DELETE FROM animal_info WHERE Animal_ID = :animal_id"
        )
        connection.execute(query, {"animal_id": animal_id})
# 添加饲养员信息到数据库
def add_caretaker(engine, name, gender, phone, responsible_area_id):
    with engine.connect() as connection:
        query = sqlalchemy.text(
            "INSERT INTO caretaker_info (Name, Gender, Phone, Responsible_Area_ID) VALUES (:name, :gender, :phone, :responsible_area_id)"
        )
        connection.execute(query, {"name": name, "gender": gender, "phone": phone, "responsible_area_id": responsible_area_id})

# 更新饲养员信息
def update_caretaker(engine, caretaker_id, name, gender, phone, responsible_area_id):
    with engine.connect() as connection:
        query = sqlalchemy.text(
            "UPDATE caretaker_info SET Name = :name, Gender = :gender, Phone = :phone, Responsible_Area_ID = :responsible_area_id WHERE Caretaker_ID = :caretaker_id"
        )
        connection.execute(query, {"caretaker_id": caretaker_id, "name": name, "gender": gender, "phone": phone, "responsible_area_id": responsible_area_id})

# 删除饲养员信息
def delete_caretaker(engine, caretaker_id):
    with engine.connect() as connection:
        query = sqlalchemy.text(
            "DELETE FROM caretaker_info WHERE Caretaker_ID = :caretaker_id"
        )
        connection.execute(query, {"caretaker_id": caretaker_id})
# 根据名称查询动物信息
def query_animals_by_name(engine, name):
    with engine.connect() as connection:
        query = sqlalchemy.text(
            "SELECT * FROM animal_info WHERE Name LIKE :name"
        )
        result = connection.execute(query, {"name": f"%{name}%"})
        return pd.DataFrame(result.fetchall(), columns=result.keys())
# 根据姓名查询饲养员信息
def query_caretakers_by_name(engine, name):
    with engine.connect() as connection:
        query = sqlalchemy.text(
            "SELECT * FROM caretaker_info WHERE Name LIKE :name"
        )
        result = connection.execute(query, {"name": f"%{name}%"})
        return pd.DataFrame(result.fetchall(), columns=result.keys())

# 主函数，定义 Streamlit 应用的布局和逻辑
def main():
    st.title("动物园管理系统")

    # 创建数据库连接
    engine = get_connection()

    # 显示数据表
    with st.expander("显示数据表"):
        if st.button('显示动物信息'):
            df_animals = pd.read_sql("SELECT * FROM animal_info", engine)
            st.write(df_animals)

        if st.button('显示饲养员信息'):
            df_caretakers = pd.read_sql("SELECT * FROM caretaker_info", engine)
            st.write(df_caretakers)

        if st.button('显示区域信息'):
            df_areas = pd.read_sql("SELECT * FROM zoo_area_info", engine)
            st.write(df_areas)

    # 添加新动物的表单
    with st.expander("添加新动物"):
        with st.form(key='add_animal_form'):
            name = st.text_input("动物名称")
            species = st.text_input("物种")
            age = st.number_input("年龄", min_value=0, value=0)
            gender = st.selectbox("性别", options=["雄性", "雌性"])
            health_status = st.text_input("健康状况")
            area_id = st.number_input("区域ID", min_value=1, value=1)

            submit_button = st.form_submit_button(label='添加动物')
            if submit_button:
                add_animal(engine, name, species, age, gender, health_status, area_id)
                st.success("已成功添加动物信息！")

    # 修改动物信息的表单
    with st.expander("修改动物信息"):
        with st.form(key='update_animal_form'):
            animal_id_upd = st.number_input("请输入需要修改的动物的ID", min_value=1, value=1)
            name_upd = st.text_input("新的动物名称")
            species_upd = st.text_input("新的物种")
            age_upd = st.number_input("新的年龄", min_value=0, value=0)
            gender_upd = st.selectbox("新的性别", options=["雄性", "雌性"])
            health_status_upd = st.text_input("新的健康状况")
            area_id_upd = st.number_input("新的区域ID", min_value=1, value=1)

            submit_button_upd = st.form_submit_button(label='更新动物信息')
            if submit_button_upd:
                update_animal(engine, animal_id_upd, name_upd, species_upd, age_upd, gender_upd, health_status_upd, area_id_upd)
                st.success("已成功更新动物信息！")

    # 删除动物信息
    with st.expander("删除动物信息"):
        animal_id_del = st.number_input("请输入需要删除的动物的ID", min_value=1, value=1)
        if st.button('删除动物信息'):
            delete_animal(engine, animal_id_del)
            st.success("已成功删除动物信息！")
    # 饲养员信息管理
    with st.expander("饲养员信息管理"):


        # 添加新饲养员的表单
        with st.form(key='add_caretaker_form'):
            name = st.text_input("饲养员姓名")
            gender = st.selectbox("性别", options=["男", "女"])
            phone = st.text_input("电话号码")
            responsible_area_id = st.number_input("负责区域ID", min_value=1, value=1)

            submit_button = st.form_submit_button(label='添加饲养员')
            if submit_button:
                add_caretaker(engine, name, gender, phone, responsible_area_id)
                st.success("已成功添加饲养员信息！")

        # 修改饲养员信息的表单
        with st.form(key='update_caretaker_form'):
            caretaker_id_upd = st.number_input("请输入需要修改的饲养员的ID", min_value=1, value=1)
            name_upd = st.text_input("新的姓名")
            gender_upd = st.selectbox("新的性别", options=["男", "女"])
            phone_upd = st.text_input("新的电话号码")
            responsible_area_id_upd = st.number_input("新的负责区域ID", min_value=1, value=1)

            submit_button_upd = st.form_submit_button(label='更新饲养员信息')
            if submit_button_upd:
                update_caretaker(engine, caretaker_id_upd, name_upd, gender_upd, phone_upd, responsible_area_id_upd)
                st.success("已成功更新饲养员信息！")

        # 删除饲养员信息
        caretaker_id_del = st.number_input("请输入需要删除的饲养员的ID", min_value=1, value=1)
        if st.button('删除饲养员信息'):
            delete_caretaker(engine, caretaker_id_del)
            st.success("已成功删除饲养员信息！")
    # 动物信息查询
    with st.expander("查询动物信息"):
        search_animal_name = st.text_input("请输入要查询的动物名称")
        if st.button('查询动物'):
            df_animals_query = query_animals_by_name(engine, search_animal_name)
            st.write(df_animals_query)

    # 饲养员信息查询
    with st.expander("查询饲养员信息"):
        search_caretaker_name = st.text_input("请输入要查询的饲养员姓名")
        if st.button('查询饲养员'):
            df_caretakers_query = query_caretakers_by_name(engine, search_caretaker_name)
            st.write(df_caretakers_query)

if __name__ == "__main__":
    main()
