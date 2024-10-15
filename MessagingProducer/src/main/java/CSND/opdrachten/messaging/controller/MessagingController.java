package CSND.opdrachten.messaging.controller;

import org.springframework.cloud.aws.messaging.core.QueueMessagingTemplate;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/message")
public class MessagingController {
    private final QueueMessagingTemplate queueMessagingTemplate;
    private final String queueTest = "FotoTestQueue";

    public MessagingController(QueueMessagingTemplate queueMessagingTemplate) {
        this.queueMessagingTemplate = queueMessagingTemplate;
    }

    @PostMapping("")
    public void createMessage() {
        String messageImSending = "hallo, dit is een test of ik een message heb gestuurd.";

        this.queueMessagingTemplate.convertAndSend(queueTest, messageImSending);
    }
}
