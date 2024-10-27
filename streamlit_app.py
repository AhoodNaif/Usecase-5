import streamlit as st
import pandas as pd
import plotly.express as px

# تحميل البيانات
df = pd.read_csv("df.csv")

# عرض العنوان
st.title("وظائف بلا خبرة؟ نعم         (ابدأ رحلتك المهنية اليوم!)")
# Raw URL of the image from GitHub
image_url = 'https://raw.githubusercontent.com/AhoodNaif/Usecase-5/main/Screenshot%202024-10-27%20031152.jpg'

# Display the image
st.image(image_url, caption='Image from GitHub', use_column_width=True)

experience_counts = df['exper'].value_counts().reset_index()
experience_counts.columns = ['Years of Experience', 'Job Postings']

# رسم بياني للأعمدة
fig = px.bar(experience_counts, 
             x='Years of Experience', 
             y='Job Postings', 
             title='توزيع الوظائف حسب متطلبات الخبرة',
             labels={'Job Postings': 'عدد الوظائف', 'Years of Experience': 'سنوات الخبرة'},
             color='Job Postings', 
             color_continuous_scale='Blues')
# Story content
st.markdown("""
متخرج جديد؟ أعرف إنك تبحث عن وظيفتك الأولى، ويمكن قاعد تفكر إن الحصول على وظيفة بدون خبرة بيكون صعب.
لكن عندي لك الخبر السعيد! البيانات توضح اليوم إن السوق يطلب الخريجين أكثر من أصحاب الخبرات.
تخيل معي، فيه 698 وظيفة ما تطلب أي خبرة، بينما الوظائف اللي تطلب خبرة هي 470 وظيفة فقط، من أصل 1168 وظيفة! 
يعني، الفرصة أمامك أكبر بكثير من اللي تتخيل!
""")
st.plotly_chart(fig)

# Continue with the story
st.markdown("""
وإذا كنت من خريجي الرياض، فأنت في المكان الصح! لأن الرياض هي المدينة اللي تعرض أكبر عدد من الوظائف بنسبة  41.9%،
تليها مكة بنسبة 25% من إجمالي الوظائف، وبعدها الشرقية. يعني لو أنت قريب من هذي المناطق، فرصتك في التوظيف 
بتكون أسرع وأقوى.
""")

# تحليل عدد الوظائف حسب المنطقة
region_counts = df['region'].value_counts().reset_index()
region_counts.columns = ['region', 'job_post_count']

# حساب نسبة كل منطقة
total_job_postings = region_counts['job_post_count'].sum()
region_counts['proportion'] = region_counts['job_post_count'] / total_job_postings

# رسم بياني دائري
fig_region = px.pie(region_counts, 
                    names='region', 
                    values='proportion', 
                    title='نسبة الوظائف حسب المنطقة في المملكة',
                    labels={'proportion': 'نسبة الوظائف'})

st.plotly_chart(fig_region)

# تحليل عدد الوظائف حسب تفضيل الجنس
gender_counts = df['gender'].value_counts().reset_index()
gender_counts.columns = ['gender', 'job_post_count']

# حساب نسبة كل تفضيل جنس
total_job_postings = gender_counts['job_post_count'].sum()
gender_counts['proportion'] = gender_counts['job_post_count'] / total_job_postings

# رسم بياني دائري
fig_gender = px.pie(gender_counts, 
                    names='gender', 
                    values='proportion', 
                    title='تفضيل الجنس في الوظائف',
                    labels={'proportion': 'نسبة الوظائف'})
# Continue with the story
st.markdown("""
أنا اذا تفكر أن الوظايف تكون موجهة لجنس معين؟ خلني أطمّنك! البيانات تقول إن أغلب الوظائف مفتوحة 
للجنسين، بنسبة 37.5%! يعني سواء كنت شاب أو فتاة، السوق مفتوح للجميع.
""")
st.plotly_chart(fig_gender)

# متوسط الرواتب حسب المسمى الوظيفي
avg_salary_by_title = df.groupby('job_title')['salary'].mean().reset_index()
fig_salary_by_title = px.bar(avg_salary_by_title, 
                              x='job_title', 
                              y='salary', 
                              title='متوسط الرواتب حسب المسمى الوظيفي',
                              labels={'salary': 'متوسط الراتب'})
# Continue with the story
st.markdown("""
أما إذا كنت لسا ما دخلت الجامعة وقاعد تفكر في مستقبلك المهني، فأنت قدام فرصة ذهبية! تبي تعرف الرواتب؟ 
عندي لك متوسط الرواتب لكل وظيفة. مثلاً، وظيفة "أخصائي بيانات ضخمة" من أعلى الوظائف أجرًا، بمتوسط راتب 7500 ريال! بينما مجمل متوسط الرواتب في السوق يبلغ 4792 ريال سعودي ولك الخيار بعد ما الصوره اصبحت جدا واضحه لك باعتقادي
""")

st.plotly_chart(fig_salary_by_title)

# متوسط الرواتب حسب المنطقة ومستوى الخبرة
avg_salary_by_region_experience = df.groupby(['region', 'exper'])['salary'].mean().reset_index()
fig_salary_by_region_experience = px.line(avg_salary_by_region_experience, 
                                           x='exper', 
                                           y='salary', 
                                           color='region',
                                           title='متوسط الرواتب حسب المنطقة ومستوى الخبرة',
                                           labels={'salary': 'متوسط الراتب', 'exper': 'سنوات الخبرة'})

st.plotly_chart(fig_salary_by_region_experience)
# Final encouragement
st.markdown("""
يا صديقي، الحين الكرة في ملعبك! السوق جاهز ينتظرك، والوظايف في انتظارك. اختر التخصص اللي يناسب ميولك 
وطموحك، وابدأ طريقك بثقة! هذا وقتك، والمستقبل بين يديك! 🎯🔥
""")
# تشغيل التطبيق
if __name__ == "__main__":
    st.write("")
