# Git/GitHub 설정 가이드

RAG_AGENT 프로젝트를 Git과 GitHub으로 관리하기 위한 완벽한 설정 가이드입니다. Git을 처음 접하거나 기본 개념을 복습하고 싶다면 이 가이드를 따라주세요.

---

## 목차

1. [사전 준비](#1-사전-준비)
2. [Git 초기 설정](#2-git-초기-설정)
3. [SSH 키 설정 (권장)](#3-ssh-키-설정-권장)
4. [새 프로젝트 시작하기](#4-새-프로젝트-시작하기)
5. [기본 워크플로우](#5-기본-워크플로우)
6. [.gitignore 설정](#6-gitignore-설정)
7. [브랜치 관리 (기본)](#7-브랜치-관리-기본)
8. [유용한 명령어](#8-유용한-명령어)
9. [자주 묻는 질문](#9-자주-묻는-질문)

---

## 1. 사전 준비

### 1.1 Git 설치 (Windows)

**옵션 A: Git for Windows 설치 (권장)**

1. https://git-scm.com/download/win 접속
2. 자동으로 다운로드되는 설치 프로그램 실행
3. 설치 과정:
   - Next를 계속 클릭
   - "Configuring the line ending conversions" 단계에서 "Checkout as-is, commit as-is" 선택 (Python 프로젝트용)
   - 나머지는 기본값 유지

4. 설치 완료 후 확인:

```bash
git --version
# 출력 예: git version 2.42.0.windows.2
```

**옵션 B: Windows Package Manager 사용**

```bash
winget install Git.Git
```

**옵션 C: Chocolatey 사용**

```bash
choco install git
```

### 1.2 GitHub 계정 생성

1. https://github.com/signup 접속
2. 이메일, 비밀번호, 사용자명 입력
3. 이메일 인증 완료
4. 프로필 설정 (선택사항이지만 권장)

---

## 2. Git 초기 설정

모든 Git 커밋에 사용될 기본 정보를 설정합니다. 이 단계는 **처음 한 번만** 수행하면 됩니다.

### 2.1 사용자 정보 설정

**전역 설정 (모든 프로젝트에 적용)**

```bash
git config --global user.name "홍길동"
git config --global user.email "hong@example.com"
```

**현재 프로젝트만 설정**

```bash
git config user.name "홍길동"
git config user.email "hong@example.com"
```

**확인 방법**

```bash
# 전역 설정 확인
git config --global --list

# 현재 프로젝트 설정 확인
git config --list
```

### 2.2 기본 에디터 설정

커밋 메시지를 에디터에서 작성할 때 사용됩니다.

**VSCode를 에디터로 사용 (권장)**

```bash
git config --global core.editor "code --wait"
```

**Notepad++ 사용**

```bash
git config --global core.editor "notepad++"
```

**기본값 유지 (Vim)**

```bash
git config --global core.editor "vim"
```

### 2.3 줄바꿈 설정 (Windows용)

Windows와 다른 OS 간의 호환성을 위해 줄바꿈 설정을 정의합니다.

```bash
# Windows에서 권장 설정 (자동 변환)
git config --global core.autocrlf true
```

이 설정은:
- 파일을 커밋할 때: CRLF → LF로 변환
- 파일을 체크아웃할 때: LF → CRLF로 변환

**확인**

```bash
git config --global core.autocrlf
# 출력: true
```

### 2.4 기타 유용한 설정

**컬러 출력 활성화**

```bash
git config --global color.ui true
```

**긴 경로 지원 (Windows)**

```bash
git config --global core.longpaths true
```

**기본 브랜치명을 main으로 설정**

```bash
git config --global init.defaultBranch main
```

---

## 3. SSH 키 설정 (권장)

SSH 키를 사용하면 매번 비밀번호를 입력하지 않고 안전하게 GitHub과 통신할 수 있습니다.

### 3.1 SSH 키 생성

**기존 SSH 키 확인**

```bash
ls -la ~/.ssh/
```

파일이 있으면 3.3으로 이동합니다.

**새 SSH 키 생성**

```bash
ssh-keygen -t ed25519 -C "hong@example.com"
```

명령어 설명:
- `-t ed25519`: 최신 보안 알고리즘 사용 (RSA보다 안전)
- `-C "hong@example.com"`: 키에 대한 설명 추가

대화식 입력:
```
> Enter file in which to save the key (/c/Users/username/.ssh/id_ed25519): [Enter 누르기]
> Enter passphrase (empty for no passphrase): [비밀번호 입력 또는 Enter]
> Enter same passphrase again: [비밀번호 재입력 또는 Enter]
```

**생성된 키 확인**

```bash
ls -la ~/.ssh/
# id_ed25519 (비공개 키)
# id_ed25519.pub (공개 키)
```

### 3.2 SSH 에이전트 설정 (Windows)

비밀번호를 매번 입력하지 않도록 SSH 에이전트를 시작합니다.

**PowerShell에서 관리자 권한으로 실행**

```powershell
# SSH 에이전트 시작
Start-Service ssh-agent

# 자동으로 시작하도록 설정
Set-Service -Name ssh-agent -StartupType Automatic
```

**비공개 키를 에이전트에 추가**

```bash
ssh-add ~/.ssh/id_ed25519
```

이 명령어를 매번 실행하지 않으려면, `~/.ssh/config` 파일을 생성하거나 수정합니다:

```
# ~/.ssh/config 파일 내용
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519
  AddKeysToAgent yes
```

### 3.3 GitHub에 공개 키 등록

**1단계: 공개 키 복사**

```bash
# Windows PowerShell
Get-Content ~/.ssh/id_ed25519.pub | Set-Clipboard

# Git Bash
cat ~/.ssh/id_ed25519.pub | clip

# WSL/Linux
cat ~/.ssh/id_ed25519.pub | xclip -selection clipboard
```

**2단계: GitHub에 등록**

1. https://github.com/settings/keys 접속
2. "New SSH key" 버튼 클릭
3. Title에 "내 Windows 노트북" 같은 설명 입력
4. Key 필드에 복사한 공개 키 붙여넣기
5. "Add SSH key" 클릭

### 3.4 SSH 연결 테스트

```bash
ssh -T git@github.com
```

**성공 메시지**
```
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

**실패 시 해결 방법**

```bash
# 상세 로그 확인
ssh -vT git@github.com
```

---

## 4. 새 프로젝트 시작하기

### 4.1 로컬에서 시작하는 경우 (로컬 폴더가 이미 있음)

**현재 디렉토리에서 Git 초기화**

```bash
cd /d/DATA/RAG_AGENT
git init
```

출력:
```
Initialized empty Git repository in D:/DATA/RAG_AGENT/.git/
```

**GitHub에서 빈 저장소 생성**

1. https://github.com/new 접속
2. Repository name: `RAG_AGENT`
3. Description: "토목설계 기준/지침 문서를 위한 RAG 시스템" (선택사항)
4. Public/Private 선택
5. "Create repository" 클릭

**원격 저장소 연결**

```bash
# SSH 사용 (권장)
git remote add origin git@github.com:username/RAG_AGENT.git

# 또는 HTTPS 사용
git remote add origin https://github.com/username/RAG_AGENT.git
```

`username`을 실제 GitHub 사용자명으로 바꾸세요.

**브랜치명 변경 및 첫 푸시**

```bash
# 기본 브랜치를 main으로 변경
git branch -M main

# 첫 커밋 전 파일 추가
git add .

# 첫 번째 커밋
git commit -m "Initial commit: RAG Agent project setup"

# GitHub에 푸시
git push -u origin main
```

### 4.2 GitHub에서 시작하는 경우 (저장소가 이미 생성됨)

**저장소 클론**

```bash
# SSH 사용 (권장)
git clone git@github.com:username/RAG_AGENT.git

# 또는 HTTPS 사용
git clone https://github.com/username/RAG_AGENT.git

# 클론된 디렉토리로 이동
cd RAG_AGENT
```

이제 모든 원격 설정이 자동으로 완료되었습니다.

---

## 5. 기본 워크플로우

### 5.1 파일 상태 확인 (git status)

작업 디렉토리의 현재 상태를 확인합니다.

```bash
git status
```

**출력 예**
```
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to stage for file...)
        modified:   README.md
        modified:   run_restructure.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        new_analysis.py
        temp_file.txt
```

**상태 해석**
- `modified`: 수정된 파일 (아직 스테이징 안 됨)
- `untracked`: Git이 추적하지 않는 새 파일

### 5.2 파일 추가 (git add)

변경사항을 스테이징 영역에 추가합니다. 이것이 다음 커밋에 포함될 파일들입니다.

**특정 파일만 추가**

```bash
git add run_restructure.py
```

**특정 패턴의 파일 추가**

```bash
# 모든 Python 파일 추가
git add *.py

# docs 폴더의 모든 파일 추가
git add docs/
```

**모든 변경사항 추가**

```bash
git add .
```

**대화식으로 추가 선택**

```bash
git add -p
```

각 변경사항에 대해 추가 여부를 묻습니다:
- `y`: 이 부분 스테이징
- `n`: 건너뛰기
- `s`: 더 작은 단위로 분할

**스테이징 확인**

```bash
git status
```

### 5.3 커밋 (git commit)

스테이징된 변경사항을 저장소에 저장합니다.

**간단한 커밋**

```bash
git commit -m "Add data restructuring function"
```

메시지 규칙:
- 명령형 동사로 시작: Add, Fix, Update, Remove, Refactor
- 첫 글자는 대문자
- 마침표로 끝내지 않음
- 50자 이내

**상세 메시지 포함**

```bash
git commit -m "Add data restructuring function" -m "
- Implement hierarchical structure conversion
- Add support for nested sections
- Include validation for section IDs
"
```

또는 에디터에서 작성:

```bash
git commit
# 에디터가 열리면 메시지 입력
# 첫 줄: 제목 (50자 이내)
# 빈 줄
# 나머지: 상세 설명 (선택사항)
```

**최근 커밋 수정**

```bash
# 파일 추가하고 커밋 수정
git add forgotten_file.py
git commit --amend --no-edit
```

### 5.4 푸시 (git push)

로컬 커밋을 GitHub으로 업로드합니다.

**첫 번째 푸시**

```bash
git push -u origin main
```

`-u` 옵션은 로컬 브랜치와 원격 브랜치를 연결합니다.

**이후 푸시**

```bash
git push
```

**특정 브랜치 푸시**

```bash
git push origin feature-branch
```

**모든 브랜치 푸시**

```bash
git push --all
```

**푸시 확인**

```bash
git log --oneline -5
# GitHub 웹사이트에서 커밋 확인
```

### 5.5 풀 (git pull)

GitHub의 최신 변경사항을 로컬로 받아옵니다.

**기본 풀**

```bash
git pull
```

이것은 `git fetch`와 `git merge`를 함께 수행합니다.

**특정 브랜치에서 풀**

```bash
git pull origin feature-branch
```

**충돌이 발생한 경우**

```
CONFLICT (content): Merge conflict in file.py
Automatic merge failed; fix conflicts and then commit the result.
```

해결 방법:

1. 파일을 열어 충돌 부분 확인
2. 충돌 마커 제거하고 코드 수정
3. 파일 저장
4. 커밋

```bash
git add file.py
git commit -m "Resolve merge conflict"
```

---

## 6. .gitignore 설정

버전 관리에서 제외할 파일을 지정합니다. Python 프로젝트와 RAG_AGENT에 맞춘 설정입니다.

### 6.1 .gitignore 파일 생성

프로젝트 루트에 `.gitignore` 파일 생성:

```bash
cd /d/DATA/RAG_AGENT
touch .gitignore
```

### 6.2 내용 추가

`/d/DATA/RAG_AGENT/.gitignore` 파일에 다음 내용 추가:

```
# Python 관련
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# 가상 환경
venv/
ENV/
env/
.venv/

# IDE 관련
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# 환경 변수 파일 (민감 정보)
.env
.env.local
.env.*.local
config_secret.py

# 데이터베이스
*.db
*.sqlite
*.sqlite3

# 로그 파일
*.log
logs/

# 임시 파일
*.tmp
temp/
*.temp
.cache/

# 원본/테스트 데이터 (선택사항: 용량이 크면 제외)
# original_data/
# raw_data/

# OS 파일
.DS_Store
Thumbs.db

# 프로젝트 특정 파일
*.xlsx
*.xls
.omc/state/
```

### 6.3 이미 커밋된 파일 제외

`.gitignore`를 추가한 후 이미 커밋된 파일을 제외하려면:

```bash
# 캐시 클리어
git rm -r --cached .

# 모든 파일 다시 추가 (이번에는 .gitignore 규칙 적용됨)
git add .

# 커밋
git commit -m "Update .gitignore and remove tracked files"
```

### 6.4 .gitignore 확인

파일이 무시되는지 확인:

```bash
git status --ignored
```

특정 파일이 왜 무시되는지 확인:

```bash
git check-ignore -v filename.py
# 출력: .gitignore:15:*.py    filename.py
```

---

## 7. 브랜치 관리 (기본)

브랜치를 사용하여 새 기능을 독립적으로 개발하고 안전하게 병합합니다.

### 7.1 브랜치 이해

**main/master 브랜치**
- 프로덕션 코드
- 항상 안정적인 상태 유지
- 직접 커밋하지 않음 (팀 규칙)

**기능 브랜치 (feature branches)**
- 새 기능 개발용
- 다양한 개발자가 동시에 작업 가능
- 테스트 후 main으로 병합

### 7.2 로컬 브랜치 생성 및 전환

**새 브랜치 생성**

```bash
git branch feature/add-vector-search
```

**브랜치 전환**

```bash
git checkout feature/add-vector-search
```

**한 번에 생성 및 전환**

```bash
git checkout -b feature/add-vector-search
```

**현재 브랜치 확인**

```bash
git branch
# 출력:
# * feature/add-vector-search
#   main
```

### 7.3 원격 브랜치 작업

**로컬 브랜치를 원격에 푸시**

```bash
# 첫 번째 푸시 (원격에 없을 때)
git push -u origin feature/add-vector-search

# 이후 푸시
git push
```

**원격 브랜치 가져오기**

```bash
# 원격 브랜치 확인
git branch -r

# 원격 브랜치 기반으로 로컬 브랜치 생성
git checkout --track origin/feature/existing-feature
```

### 7.4 브랜치 병합

**main 브랜치로 이동**

```bash
git checkout main
```

**main을 최신 상태로 업데이트**

```bash
git pull origin main
```

**feature 브랜치 병합**

```bash
git merge feature/add-vector-search
```

**충돌 해결**

```bash
# 병합 중 충돌이 발생한 경우
# 1. 파일 열어서 충돌 부분 수정
# 2. 파일 저장
# 3. 스테이징 및 커밋

git add .
git commit -m "Merge feature/add-vector-search"
```

**병합 취소**

```bash
git merge --abort
```

### 7.5 브랜치 삭제

**로컬 브랜치 삭제**

```bash
# 안전 삭제 (병합된 브랜치만)
git branch -d feature/add-vector-search

# 강제 삭제
git branch -D feature/add-vector-search
```

**원격 브랜치 삭제**

```bash
git push origin --delete feature/add-vector-search
```

### 7.6 브랜치 명명 규칙 (권장)

```
feature/기능설명          - 새 기능 추가
fix/버그설명            - 버그 수정
docs/문서설명           - 문서 작성/수정
refactor/리팩토링설명    - 코드 리팩토링
test/테스트설명         - 테스트 추가
```

**예시**
```
feature/add-vector-search
feature/implement-graphrag
fix/database-connection-issue
docs/update-readme
test/add-chunking-tests
```

---

## 8. 유용한 명령어

### 8.1 커밋 히스토리 확인 (git log)

**간단한 로그 (한 줄)**

```bash
git log --oneline
```

출력:
```
a1b2c3d Add vector search implementation
f4e5d6c Update database schema
7g8h9i0 Initial commit
```

**상세 로그**

```bash
git log
```

**특정 파일의 히스토리**

```bash
git log run_restructure.py
```

**특정 브랜치의 로그**

```bash
git log origin/main..HEAD
# 원격의 main과 로컬 현재 브랜치의 차이
```

**시각적 로그**

```bash
git log --graph --oneline --all
```

### 8.2 변경사항 확인 (git diff)

**스테이징 전 변경사항 확인**

```bash
git diff
```

**스테이징된 파일의 변경사항**

```bash
git diff --staged
```

**특정 파일의 변경사항**

```bash
git diff run_restructure.py
```

**두 커밋 간 차이**

```bash
git diff a1b2c3d f4e5d6c
```

**마지막 커밋과의 차이**

```bash
git diff HEAD
```

### 8.3 스테이싱 (git stash)

작업 중인 변경사항을 임시로 저장하고 나중에 복원합니다.

**변경사항 임시 저장**

```bash
git stash
```

또는 메시지와 함께:

```bash
git stash save "WIP: vector search implementation"
```

**임시 저장된 목록 확인**

```bash
git stash list
```

출력:
```
stash@{0}: WIP: vector search implementation
stash@{1}: On main: database schema update
```

**임시 저장 복원**

```bash
# 가장 최근 스태시 복원
git stash pop

# 특정 스태시 복원
git stash pop stash@{1}

# 복원 후 스태시 유지
git stash apply stash@{0}
```

**스태시 삭제**

```bash
# 특정 스태시 삭제
git stash drop stash@{0}

# 모든 스태시 삭제
git stash clear
```

### 8.4 커밋 되돌리기

**가장 최근 커밋 취소 (파일 유지)**

```bash
git reset --soft HEAD~1
```

**가장 최근 커밋 취소 (변경사항 유지)**

```bash
git reset --mixed HEAD~1
```

**특정 커밋으로 돌아가기**

```bash
git revert a1b2c3d
```

`revert`는 새 커밋을 만들어 변경사항을 취소합니다 (권장).

**위험: 모든 변경사항 취소**

```bash
git reset --hard origin/main
```

위험: 로컬 변경사항이 모두 삭제됩니다. 신중히 사용하세요.

### 8.5 원격 저장소 정보

**원격 저장소 확인**

```bash
git remote -v
```

출력:
```
origin  git@github.com:username/RAG_AGENT.git (fetch)
origin  git@github.com:username/RAG_AGENT.git (push)
```

**원격 브랜치 동기화**

```bash
git fetch origin
```

이것은 원격 변경사항을 다운로드하지만 병합하지 않습니다.

**원격 브랜치 추적**

```bash
git branch -vv
```

각 브랜치가 어느 원격 브랜치를 추적하는지 확인합니다.

---

## 9. 자주 묻는 질문

### Q1: 실수로 파일을 삭제했는데 복구할 수 있나요?

**답변:**

마지막 커밋에서 복구 가능:

```bash
git checkout HEAD -- filename.py
```

특정 커밋에서 복구:

```bash
git checkout a1b2c3d -- filename.py
```

### Q2: 커밋 메시지를 수정하고 싶어요.

**답변:**

마지막 커밋 메시지만 수정:

```bash
git commit --amend -m "새로운 메시지"
```

에디터에서 수정:

```bash
git commit --amend
```

### Q3: 특정 커밋을 제거하고 싶어요.

**답변:**

```bash
# 커밋 로그 확인
git log --oneline

# 특정 커밋 되돌리기 (새 커밋으로 변경사항 취소)
git revert a1b2c3d
```

### Q4: 브랜치를 실수로 삭제했어요.

**답변:**

최근 삭제된 브랜치 복구:

```bash
# 최근 참조 확인
git reflog

# 브랜치 복구
git checkout -b feature/branch-name a1b2c3d
```

### Q5: 충돌이 발생했는데 어떻게 해야 하나요?

**답변:**

1. 충돌이 발생한 파일 확인:

```bash
git status
```

2. 파일 열어서 충돌 마커 확인:

```
<<<<<<< HEAD
로컬 변경사항
=======
원격 변경사항
>>>>>>> feature/branch
```

3. 하나를 선택하거나 병합:

```python
# 예: 두 변경사항 모두 유지
합친 코드
```

4. 파일 저장 후 커밋:

```bash
git add file.py
git commit -m "Resolve merge conflict"
```

### Q6: 원격 저장소에 이미 푸시한 커밋을 수정할 수 있나요?

**답변:**

**권장하지 않음** (타인의 작업을 방해할 수 있음)

본인만 사용하는 브랜치면:

```bash
git commit --amend
git push --force-with-lease
```

`--force-with-lease`를 사용하세요 (더 안전함).

팀 프로젝트면 새 커밋으로 변경사항을 취소하는 것이 낫습니다:

```bash
git revert a1b2c3d
git push
```

### Q7: Git 설정을 확인하려면?

**답변:**

모든 설정 확인:

```bash
git config --list
```

특정 항목 확인:

```bash
git config user.name
git config core.editor
```

### Q8: 대용량 파일이 있는데 어떻게 하나요?

**답변:**

`.gitignore`에 추가:

```
# .gitignore
*.xlsx
*.bin
large_data/
```

또는 Git LFS (Large File Storage) 사용:

```bash
# Git LFS 설치
winget install GitHub.GitLFS

# 초기화
git lfs install

# 추적할 파일 타입 지정
git lfs track "*.xlsx"

# .gitattributes 커밋
git add .gitattributes
```

### Q9: 여러 GitHub 계정을 사용하려면?

**답변:**

SSH 설정에서 여러 키 지정:

```
# ~/.ssh/config
Host github.com-personal
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519

Host github.com-work
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_work
```

저장소마다 원격 설정:

```bash
# 개인 저장소
git remote set-url origin git@github.com-personal:personal-username/repo.git

# 업무 저장소
git remote set-url origin git@github.com-work:work-username/repo.git
```

### Q10: Push 후 실수로 잘못된 내용을 올렸어요.

**답변:**

로컬에서 수정 후 강제 푸시 (신중히!):

```bash
# 로컬에서 수정
git commit --amend

# 강제 푸시 (더 안전한 옵션)
git push --force-with-lease
```

또는 새 커밋으로 되돌리기 (권장, 협업할 때):

```bash
git revert a1b2c3d
git push
```

---

## 10. 추가 리소스

### 공식 문서
- [Git 공식 문서](https://git-scm.com/doc)
- [GitHub 도움말](https://docs.github.com)

### 학습 자료
- [Interactive Git Tutorial](https://learngitbranching.js.org/)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)

### 설정 파일 예시

**프로젝트별 .gitignore**

완성된 예시는 `/.gitignore` 파일을 참고하세요.

**SSH config**

`~/.ssh/config` 파일을 수동으로 생성하거나 위의 3.2 섹션을 참고하세요.

---

## 11. 빠른 참조표

| 작업 | 명령어 |
|------|--------|
| 저장소 초기화 | `git init` |
| 저장소 클론 | `git clone git@github.com:user/repo.git` |
| 현재 상태 확인 | `git status` |
| 파일 추가 | `git add filename` |
| 모든 파일 추가 | `git add .` |
| 커밋 | `git commit -m "메시지"` |
| GitHub 푸시 | `git push` |
| GitHub에서 받기 | `git pull` |
| 브랜치 생성 | `git checkout -b branch-name` |
| 브랜치 전환 | `git checkout branch-name` |
| 브랜치 병합 | `git merge branch-name` |
| 커밋 로그 | `git log --oneline` |
| 변경사항 확인 | `git diff` |
| 변경사항 임시 저장 | `git stash` |
| 임시 저장 복원 | `git stash pop` |
| 원격 저장소 확인 | `git remote -v` |
| 원격 업데이트 확인 | `git fetch origin` |
| 마지막 커밋 수정 | `git commit --amend` |
| 특정 파일 되돌리기 | `git checkout HEAD -- filename` |

---

## 번호 정보

**작성일**: 2026년 2월 5일
**Git 버전**: 2.42.0 이상
**대상**: Python/RAG 프로젝트 개발자
**언어**: 한국어

---

이 가이드가 RAG_AGENT 프로젝트의 Git/GitHub 관리에 도움이 되길 바랍니다. 추가 질문이 있으시면 FAQ 섹션을 참고하거나 Git 공식 문서를 확인하세요.
