# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.corehr.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: PatchJobDataRequest = PatchJobDataRequest.builder() \
        .job_data_id("151515") \
        .client_token("12454646") \
        .user_id_type("people_corehr_id") \
        .department_id_type("people_corehr_department_id") \
        .request_body(JobData.builder()
                      .job_level_id("6890452208593372679")
                      .job_grade_id("6890452208593372679")
                      .employee_type_id("6890452208593372679")
                      .working_hours_type_id("6890452208593372679")
                      .work_location_id("6890452208593372679")
                      .department_id("6890452208593372679")
                      .job_id("6890452208593372679")
                      .probation_start_date("2018-03-16T00:00:00")
                      .probation_end_date("2019-05-24T00:00:00")
                      .primary_job_data(True)
                      .employment_id("6893014062142064135")
                      .effective_time("2020-05-01 00:00:00")
                      .expiration_time("2020-05-02 00:00:00")
                      .job_family_id("1245678")
                      .assignment_start_reason(Enum.builder().build())
                      .probation_expected_end_date("2006-01-02")
                      .direct_manager_id("6890452208593372679")
                      .dotted_line_manager_id_list([])
                      .second_direct_manager_id("6890452208593372679")
                      .cost_center_rate([])
                      .custom_fields([])
                      .build()) \
        .build()

    # 发起请求
    response: PatchJobDataResponse = client.corehr.v1.job_data.patch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v1.job_data.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
