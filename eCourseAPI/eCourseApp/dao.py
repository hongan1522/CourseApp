from  eCourseApp.models import Category, Course, Lesson

def get_courses(**kwargs):
    courses = Course.objects.filter(active=True)

    q = kwargs.get('q')
    if q:
        courses = courses.filter(name_icontain=q)

    cate_id = kwargs.get('category_id')
    if cate_id:
        courses = courses.filter(category_id=cate_id)

    return courses.order_by('-id')

def count_course_by_cate():
    return Category.objects.annotate(counter=Count('course_set')).values('id', 'name', 'counter').all()