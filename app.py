import streamlit as st

# Cấu hình giao diện trang
st.set_page_config(page_title="Tính Lãi Suất Tiết Kiệm", page_icon="💰", layout="centered")

st.title("💰 Ứng dụng Tính Lãi Suất Tiết Kiệm")
st.markdown("Nhập thông tin khoản tiết kiệm của bạn bên dưới để xem chi tiết tiền lãi và tổng số tiền nhận được.")

# Form nhập liệu
with st.form("savings_form"):
    principal = st.number_input(
        "Số tiền gửi (VNĐ):", 
        min_value=0.0, 
        value=50000000.0, 
        step=1000000.0, 
        format="%.0f"
    )
    
    months = st.number_input(
        "Kỳ hạn gửi (tháng):", 
        min_value=1, 
        max_value=360, 
        value=12, 
        step=1
    )
    
    annual_rate = st.number_input(
        "Lãi suất (%/năm):", 
        min_value=0.0, 
        max_value=100.0, 
        value=6.0, 
        step=0.1
    )
    
    payout_method = st.selectbox(
        "Hình thức nhận lãi:",
        ("Cuối kỳ", "Hàng tháng", "Hàng quý")
    )
    
    submitted = st.form_submit_button("Tính Toán")

# Xử lý khi người dùng bấm nút tính toán
if submitted:
    # Tính lãi suất theo tháng
    monthly_rate = (annual_rate / 100) / 12
    
    if payout_method == "Hàng tháng":
        periodic_interest = principal * monthly_rate
        total_interest = periodic_interest * months
        periodic_label = "Tiền lãi định kỳ (Hàng tháng)"
    elif payout_method == "Hàng quý":
        periodic_interest = principal * monthly_rate * 3
        num_quarters = months / 3
        total_interest = periodic_interest * num_quarters
        periodic_label = "Tiền lãi định kỳ (Hàng quý)"
    else:  # Cuối kỳ
        total_interest = principal * (annual_rate / 100) * (months / 12)
        periodic_interest = total_interest  # Nhận 1 lần toàn bộ vào cuối kỳ
        periodic_label = "Tiền lãi nhận cuối kỳ"

    total_amount = principal + total_interest

    # Hiển thị kết quả dạng các khối thống kê (Metrics)
    st.markdown("---")
    st.subheader("📊 Kết quả tính toán")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label=periodic_label, value=f"{periodic_interest:,.0f} VNĐ")
        st.metric(label="Tổng tiền lãi", value=f"{total_interest:,.0f} VNĐ")
        
    with col2:
        st.metric(label="Tiền gốc ban đầu", value=f"{principal:,.0f} VNĐ")
        st.metric(label="Tổng gốc và lãi", value=f"{total_amount:,.0f} VNĐ")
        
    # Bảng tóm tắt thông số
    st.markdown("---")
    st.markdown("### 📋 Tóm tắt thông tin khoản gửi")
    st.info(f"""
    - **Số tiền gửi:** {principal:,.0f} VNĐ
    - **Kỳ hạn:** {months} tháng
    - **Lãi suất:** {annual_rate}% / năm
    - **Hình thức nhận lãi:** {payout_method}
    """)
