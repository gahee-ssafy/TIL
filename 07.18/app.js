// 채팅 전송 및 수신을 위한 선택
const chatInput = document.querySelector('.chat-input')
// const chatSubmitIcon = document.querySelector('.chat-submit-icon')
const chatContainer = document.querySelector('.chat-area')

// 채팅창에 내용을 추가해주는 부분
const addChat = (type, value) => {
  const chat = document.createElement('div')
  chat.classList.add('chat')
  chat.innerText = value
  chat.classList.add(`${type}-chat`)
  chatContainer.appendChild(chat)
  chatContainer.scrollTop = chatContainer.scrollHeight
}

// 1. 챗봇 서버에 요청할 URL (chatGPT API reference Chat 파트 참고)
const OPEN_API_URL = 'https://api.openai.com/v1/chat/completions'
// 2. API 키 (발급 받은 Secret Key)
const API_KEY = '' // 
// 필요한 헤더 정보
const headers = {
  Authorization: `Bearer ${API_KEY}`, // 인증 키 설정
  'Content-Type': 'application/json' // 요청 데이터의 타입
}


// 모든 대화 메시지를 저장하는 배열 (대화 맥락 유지)
let messagesHistory = [];

// 유머 스타일을 지정하는 시스템 프롬프트
const systemPrompt = {
  role: 'system',
  content: '너는 이제부터 노래 부르기 챗봇이야. 사용자의 질문이나 대화에 항상 노래 가사처럼 운율을 넣어 답변해줘. 실제 존재하는 노래의 가사 스타일을 참고하거나, 창의적으로 새로운 가사처럼 만들어도 좋아. 답변은 반드시 노래처럼 2~4줄로 구성해줘.'
};



const chatReceive = (userMsg) => {
  // 첫 메시지라면 system 프롬프트를 추가
  if (messagesHistory.length === 0 || messagesHistory[0].role !== 'system') {
    messagesHistory.unshift(systemPrompt);
  }
  // 사용자의 메시지를 messagesHistory에 추가
  messagesHistory.push({
    role: 'user',
    content: userMsg
  });

  // chatGPT API 서버에 요청을 보내는 부분
  axios({
    method: 'post',
    url: OPEN_API_URL,
    headers,
    data: {
      model: 'gpt-4o-mini',
      messages: messagesHistory // 누적된 대화 맥락 전달
    }
  })
  //  chatGPT API 서버에서 정상적으로 응답이 도달했을 때 실행되는 부분
    .then(res => {
      // 응답 데이터 확인 (크롬 개발자 도구 콘솔창)
      console.log(res.data);

      // 1. 응답 데이터에서 응답 메세지를 가져온다.
      let response = res.data.choices[0].message.content;

      // 2. 강아지(시츄) 이모티콘을 랜덤하게 추가
      const dogEmojis = ['🐶', '🦴', '🐾', '🦮', '🐕‍🦺', '🐕', '💛'];
      const randomEmoji = dogEmojis[Math.floor(Math.random() * dogEmojis.length)];
      response = response + ' ' + randomEmoji;

      // 3. 채팅창에 메세지를 등록한다.
      addChat('receive', response);

      // 4. assistant의 응답을 messagesHistory에 추가 (대화 맥락 유지)
      messagesHistory.push({
        role: 'assistant',
        content: response
      });
    })
    // 요청에 있어 잘못된 설정이나 서버에 문제가 있을 때 실행되는 부분
    .catch(err => {
      console.log(err.response.data) // 에러 데이터
      console.log(err.response.status) // 4xx : 사용자 실수, 5xx : 서버 문제
    })
}

const chatSubmit = () => {
  const value = chatInput.value
  if (!value) return
  addChat('send', value)
  chatReceive(value)
  chatInput.value = ''
}


chatInput.addEventListener('keyup', (e) => {
  e.key === 'Enter' && chatSubmit()
})

// 다크/라이트 모드 토글 기능 (항상 노란색 배경 유지)
const themeToggleBtn = document.getElementById('theme-toggle');
const body = document.body;
themeToggleBtn.addEventListener('click', () => {
  body.classList.toggle('dark-mode');
  body.style.background = '#ffe066';
  if (body.classList.contains('dark-mode')) {
    themeToggleBtn.textContent = '☀️';
  } else {
    themeToggleBtn.textContent = '🌙';
  }
});
