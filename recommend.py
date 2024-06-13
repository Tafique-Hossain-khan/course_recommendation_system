
import pandas as pd
import preprocessing




#clean_data = preprocessing.pre_process(df)

def recommend_courses(df,text):

    clean_data = preprocessing.update_df(df)

    #get the specific index of a title
    course_index = pd.Series(index=clean_data['course_title'],data=clean_data.index).drop_duplicates()
    index = course_index[text]
    cos_sim = preprocessing.get_consing_mat(clean_data)
    enumerated_scores = list(enumerate(cos_sim[index]))
    sorted_scores = sorted(enumerated_scores, key=lambda x: x[1], reverse=True)[1:]

    sorted_index = [i[0] for i in sorted_scores]
    sorted_score = [i[1] for i in sorted_scores]
    temp_df = clean_data.iloc[sorted_index]

    temp_df['similarity_score'] = sorted_score

    final_recommended_course = temp_df[['course_title','url','similarity_score','price']]
    final_recommended_course = final_recommended_course[final_recommended_course['similarity_score']>=0.5].head(5)
    course_url = list(final_recommended_course['url'])
    course_title = list(final_recommended_course['course_title'])
    #course_price = list(df['url'])

    return course_title,course_url
    #return final_recommended_course