from fastapi import APIRouter

from typing import List

router = APIRouter()



# 목업 데이터: 3일차에 실제 CSV 데이터로 교체한다

MOCK_JOBS = [

    {
        "id": 1,
        "company": "카카오",
        "title": "백엔드 개발자",
        "required_skills": ["Python", "FastAPI", "PostgreSQL"],
        "preferred_skills": ["Docker", "Redis", "AWS"],
        "description": "서비스 API를 설계·개발하고, 사용자 데이터를 안정적으로 처리하는 백엔드 시스템을 운영합니다. 통계 기반 지표를 활용한 기능 개선과 성능 최적화에도 참여합니다.",
        "deadline": "2026-08-31"
    },

    {

        "id": 2,
        "company": "카카오",
        "title": "데이터 엔지니어",
        "required_skills": ["Python", "SQL", "Pandas"],
        "preferred_skills": ["Airflow", "Spark", "dbt"],
        "description": "채용·서비스 데이터를 수집·정제·적재하는 데이터 파이프라인을 구축합니다. 분석팀과 협업해 신뢰할 수 있는 데이터 마트를 제공하고, 데이터 품질을 지속적으로 관리합니다.",
        "deadline": "2026-08-15"

    },

    {

        "id": 3,
        "company": "네이버클라우드",
        "title": "ML 엔지니어",
        "required_skills": ["Python", "PyTorch", "통계"],
        "preferred_skills": ["MLOps", "Docker", "LangChain"],
        "description": "추천·분류 등 ML 모델을 학습·배포하고, 서비스 환경에서 모델 성능을 모니터링합니다. A/B 테스트와 통계적 검증을 통해 모델 개선 효과를 측정합니다.",
        "deadline": "2026-07-31"

    }

]



@router.get("/jobs", tags=["Jobs"])

def get_jobs():

    """

    취업 공고 목록을 반환하는 엔드포인트.

    현재는 목업 데이터를 반환하며, 3일차에 실제 데이터로 교체한다.

    """

    return {

        "count": len(MOCK_JOBS),

        "jobs": MOCK_JOBS

    }



@router.get("/jobs/{job_id}", tags=["Jobs"])

def get_job_by_id(job_id: int):

    """

    특정 공고의 상세 정보를 반환한다.

    """

    for job in MOCK_JOBS:

        if job["id"] == job_id:

            return job

    # 찾지 못한 경우

    from fastapi import HTTPException

    raise HTTPException(status_code=404, detail=f"공고 ID {job_id}를 찾을 수 없습니다.")